from __future__ import annotations

import logging
from typing import TYPE_CHECKING

import numpy as np
import sounddevice as sd

if TYPE_CHECKING:
    from whispy.notify import Notify

logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.INFO)

SAMPLE_RATE = 16000


class Recorder:
    def __init__(self, notify: Notify) -> None:
        self._rec = False
        self._stream = None
        self._data = []
        self._notify = notify

    def start(self) -> None:
        self._rec = True
        self._data = []
        self._stream = sd.InputStream(
            callback=self._callback, channels=1, samplerate=SAMPLE_RATE,
        )
        self._stream.start()
        self._notify("Transcribing started", urgency="critical")

    def stop(self) -> tuple[None, None] | tuple[float, np.ndarray]:
        if not self._rec:
            return (None, None)

        self._rec = False
        assert self._stream
        self._stream.stop()
        self._stream.close()
        self._stream = None
        self._notify("Transcribing ended")

        if self._data == []:
            return (None, None)

        audio_data_np = np.concatenate(self._data, axis=0)
        audio_data_length = len(audio_data_np) / SAMPLE_RATE

        return (audio_data_length, audio_data_np)

    @property
    def recording(self) -> bool:
        return self._rec

    def _callback(self, indata, frames, time, status) -> None:  # noqa: ANN001, ARG002
            # Check if indata has the expected shape (e.g., (32,))
        if self._rec and indata.shape[1] == 1:  # Check if indata is mono
                self._data.append(indata.copy())
