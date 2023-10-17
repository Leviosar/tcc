import os
import logging

from datetime import datetime
from steganossaurus.constants import ROOT_DIR
from typing import Literal

try:
    os.mkdir(f"{ROOT_DIR}/logs")
except:
    pass


def setup_logger(
    level: Literal["debug", "info", "warning", "error", "critical"] = "warning"
):
    levels = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL,
    }

    logging.basicConfig(
        filename=f"{ROOT_DIR}/logs/{datetime.today().strftime('%Y-%m-%d')}.log",
        level=levels.get(level),
        format="[%(asctime)s] - [%(levelname)s]: %(message)s",
        datefmt="%H:%M:%S",
    )
