# Built in
import logging

LOG_LEVEL = logging.INFO

logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s     %(message)s.", datefmt="%Y-%m-%d %H:%M:%S"
)

file_handler = logging.FileHandler(
    filename="logs/discord.log", encoding="utf-8", mode="w"
)
file_handler.setLevel(LOG_LEVEL)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
