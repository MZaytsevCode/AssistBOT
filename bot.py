# bot.py
# Recycled 06/15/20
import os

from discord.ext import commands

client = commands.Bot(command_prefix='!')


@client.command()
async def load(extension):
    """Load cogs"""
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(extension):
    """Unload cogs"""
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

token = os.environ.get('BOT_TOKEN')
client.run(str(token))
