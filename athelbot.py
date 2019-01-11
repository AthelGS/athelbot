import os
import discord
import random
from discord import Game
from discord.ext.commands import Bot

# Set everything up before the bot runs
quotes = []
quote_choice = 0

if os.path.exists("athelbotcfg.txt"):
	with open("athelbotcfg.txt") as f:
		for line in f:
			line = line.strip()
			quotes.append(line)
else:
	quotes = ["Test quote 1",
	"Test quote 2",
	"Test quote 3"]

# Important bot stuff
BOT_PREFIX = ('a-')
TOKEN = os.environ['BOT_TOKEN']
client = Bot(command_prefix = BOT_PREFIX)

@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(name="On the beta branch!", type=1))

# The commands
@client.command()
async def test():
	await client.say("pong")

@client.command()
async def quote(number):
	if number == "random":
		quote_choice = random.randint(o, len(quotes))
	else:
		quote_choice = number
	
	embed = discord.Embed(title="Athel Quote", description=quotes[quote_choice], color=0x00ffff)
	embed.set_footer(text= "Quote #" + str(quote_choice) + " of " + str(len(quotes) + " quotes.")
	#await client.send_message(message.channel, embed=embed)

# Run the bot
client.run(TOKEN)

# This is called when the bot is closed.
if os.path.exists("athelbotcfg.txt"):
	os.remove("athelbotcfg.txt")

f = open("athelbotcfg.txt", "w+")

for item in quotes:
	f.write("%s\n" % item);
	
f.close()
