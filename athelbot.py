import os
import discord
import random
from discord import Game
from discord.ext.commands import Bot

quotes = []
if os.path.exists("athelbotcfg.txt"):
	with open("athelbotcfg.txt") as f:
		for line in f:
			line = line.strip()
			quotes.append(line)
else:
	quotes = ["Test quote 1",
	"Test quote 2",
	"Test quote 3"]
	
BOT_PREFIX = ('a-')
TOKEN = os.environ['BOT_TOKEN']

client = Bot(command_prefix = BOT_PREFIX)

@client.command()
async def test():
	await client.say("pong")

@client.command()
async def quote(number):
	if number == None:
		await client.say("quote")

client.run(TOKEN)


if os.path.exists("athelbotcfg.txt"):
	os.remove("athelbotcfg.txt")

f = open("athelbotcfg.txt", "w+")

for item in quotes:
	f.write("%s\n" % item);
	
f.close()
