"""
This module is reponsible for the creation and configure the logger that can be used on this microservice.
To use the this logger on other modules, just import it and use it.
"""

import os
from dotenv import load_dotenv
import logging
from rich.logging import RichHandler

load_dotenv()
logging_level = os.getenv("LOGGING_LEVEL")

if logging_level == "DEBUG":
    logger_level = logging.DEBUG
elif logging_level == "INFO":
    logger_level = logging.INFO
else:
    logger_level = logging.WARNING

logging.basicConfig(
    format="[%(asctime)s]: [%(levelname)8s]: %(message)s (%(filename)s:%(lineno)s)",
    level=logger_level,
    datefmt="%m.%d.%Y %H:%M:%S",
    handlers=[RichHandler(show_time=False, show_level=False)],
)
