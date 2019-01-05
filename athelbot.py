import os
import discord
import random
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ('a-')
TOKEN = os.environ['BOT_TOKEN']

client = Bot(command_prefix = BOT_PREFIX)

@client.command()
async def test():
	await client.say("pong")
	
client.run(TOKEN)
