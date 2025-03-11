import logging
from dataclasses import dataclass

import numpy as np
from pynput.keyboard import Key, Listener

from whispy.notify import Notify
from whispy.record import Recorder
from whispy.transform import Transformer
from whispy.typewriter import Writer


class Transcriber:
    def __init__(self, model: str) -> None:
        logging.info("Loading model: %s", model)
        import whisper

        self._model = whisper.load_model("small.en")

    def __call__(self, data: np.ndarray) -> str:
        result = self._model.transcribe(
            data.flatten().astype(np.float32),
            fp16=False,
        )
        return f"{result['text']}".strip()


@dataclass
class _T:
    transformer: Transformer
    name: str
    priority: int


class WhispyListener(Listener):
    def __init__(
        self,
        rkey: Key,
        notify: Notify,
        writer: Writer,
        transcriber: Transcriber,
        *transformers: tuple[Key, Transformer, str],
    ) -> None:
        super().__init__(on_press=self._on_press, on_release=self._on_release) # type: ignore
        self._rkey = rkey
        self._notify = notify
        self._writer = writer
        self._rec = Recorder(notify)
        self._transcriber = transcriber
        self._cancel = False

        self._transformers = {
            k: _T(t, n, i) for i, (k, t, n) in enumerate(transformers)
        }
        self._active_trans = []

    def _on_press(self, key: Key) -> None:
        if self._rec.recording:
            if key == Key.esc:
                self._notify("Canceled by user", urgency="low")
                self._cancel = True

            transformer = self._transformers.get(key)
            if transformer:
                self._notify(f"Enabled transformer: {transformer.name}", urgency="low")
                self._active_trans.append(transformer)

        if key != self._rkey:
            return

        self._rec.start()

    def _on_release(self, key: Key) -> None:
        if key != self._rkey:
            return

        should_cancel = self._cancel
        self._cancel = False

        transformers: list[_T] = list(self._active_trans)
        self._active_trans = []
        transformers.sort(key=lambda t: t.priority)

        data_len, data = self._rec.stop()
        if not data_len or data is None:
            logging.info("Recording has no data, skipping")
            return

        if should_cancel:
            logging.info("Recording cancelled, skipping")
            return

        if data_len < 0.5:
            logging.info("Recording to short, skipping")
            return

        logging.info("Transcribing audio")
        transcript_text = self._transcriber(data)
        logging.info("Transcript:\n> %s", transcript_text)

        for t in transformers:
            logging.info("Applying transformer: %s", t.name)
            transcript_text = t.transformer(transcript_text)
            logging.info("Result:\n> %s", transcript_text)

        logging.info("Typing result")
        self._writer(transcript_text + " ")
