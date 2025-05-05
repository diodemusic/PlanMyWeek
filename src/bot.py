# 3rd party
import discord
from discord import app_commands

# My code
from logger import logger
import secret_tokens

TEST_GUILD_ID = secret_tokens.Secret.TEST_SERVER_ID.value


@app_commands.command(name="plan", description="Plan my week :).")
async def plan(
    interaction: discord.Interaction,
    moudle1: str,
    moudle2: str,
    moudle3: str = None,
    moudle4: str = None,
):
    if moudle3 is None:
        moudle3 = ""

    if moudle4 is None:
        moudle4 = ""

    await interaction.response.send_message(
        f"hello :) {moudle1}\n{moudle2}\n{moudle3}\n{moudle4}"
    )


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    def clear_commands(self):
        try:
            # TODO remove in prod
            self.tree.clear_commands(self.get_guild(TEST_GUILD_ID), type=None)
            logger.info("Commands cleared.")
        except Exception as e:
            logger.info(f"Error clearing commands: {e}")

    def add_command(self, command):
        try:
            # TODO remove in prod
            self.tree.add_command(command, guild=self.get_guild(TEST_GUILD_ID))
            logger.info(f"Command added: {command}")
        except Exception as e:
            logger.info(f"Error adding command: {e}")

    async def sync_tree(self):
        try:
            # TODO remove in prod
            commands = await self.tree.sync(guild=self.get_guild(TEST_GUILD_ID))
            logger.info(f"Commands synchronized: {commands}")
        except Exception as e:
            logger.info(f"Error syncing commands: {e}")

    async def setup_hook(self):
        self.clear_commands()
        await self.sync_tree()
        self.add_command(plan)
        await self.sync_tree()


intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    logger.info(f"Logged in as {client.user}")

    for guild in client.guilds:
        logger.info(f"Connected to guild: {guild.name} (ID: {guild.id})")


def main():
    client.run(token=secret_tokens.Secret.DISCORD_BOT_TOKEN.value)
