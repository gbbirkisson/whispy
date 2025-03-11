import logging
import subprocess

from typing_extensions import Protocol


class Notify(Protocol):
    def __call__(self, msg: str, urgency: str = "normal") -> None: ...


def cmd_notify_send(msg: str, urgency: str = "normal") -> None:
    logging.info(msg)
    subprocess.run(["notify-send", "-u", urgency, "-t", "5000", msg], check=False)
