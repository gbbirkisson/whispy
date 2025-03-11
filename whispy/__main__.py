import logging

import click
from openai import OpenAI
from pynput.keyboard import Key

from whispy.notify import cmd_notify_send
from whispy.transcribe import Transcriber, WhispyListener
from whispy.transform import Emailer, Translator
from whispy.typewriter import cmd_xdotool

logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.INFO)


@click.command()
@click.option(
    "--model",
    "-m",
    default="small.en",
    show_default=True,
    help="Whisper model to use.",
)
@click.option(
    "--translate",
    "-t",
    default="norwegian",
    show_default=True,
    help="Language to translate to.",
)
@click.option(
    "--openai-api-key",
    "-k",
    envvar="OPENAI_API_KEY",
    help="OpenAI API key.  [env: OPENAI_API_KEY]",
)
def _whispy(model: str, translate: str, openai_api_key: str) -> None:
    """Simple program that transcribes audio when a hotkey is pressed. Once the program has
    started, these are the keys you can use:

        \b
        RIGHT_CTRL: Press and hold to start recording audio
        RIGHT_SHIFT: Press briefly while recording to translate transcript
        LEFT_SHIFT: Press briefly while recording to output email
        ESC: Press briefly while recording to cancel
    """
    openai_client = OpenAI(api_key=openai_api_key)

    with WhispyListener(
        Key.ctrl_r,
        cmd_notify_send,
        cmd_xdotool,
        Transcriber(model),
        (
            Key.shift_l,
            Emailer(openai_client),
            "Emailer",
        ),
        (
            Key.shift_r,
            Translator(openai_client, translate),
            f"Translator ({translate})",
        ),
    ) as listener:
        logging.info("Ready to transcribe")
        try:
            listener.join()
        except KeyboardInterrupt:
            logging.info("Exiting")


def main() -> None:
    _whispy()


if __name__ == "__main__":
    main()
