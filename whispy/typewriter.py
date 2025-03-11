import subprocess

from typing_extensions import Protocol


class Writer(Protocol):
    def __call__(self, msg: str) -> None: ...


def cmd_xdotool(msg: str, delay: int = 10) -> None:
    for nr, line in enumerate(msg.splitlines()):
        if nr > 1:
            subprocess.run(["xdotool", "key", "Return"])
        subprocess.run(["xdotool", "type", "--delay", f"{delay}", line])
