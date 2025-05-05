# Built in
from enum import Enum

# 3rd party
from dotenv import dotenv_values

_SECRETS = dotenv_values(".env")


class Secret(Enum):
    DISCORD_BOT_TOKEN = _SECRETS.get("DISCORD_BOT_TOKEN")
    TEST_SERVER_ID = _SECRETS.get("TEST_SERVER_ID")
