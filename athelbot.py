import os
import discord
import random
import asyncio
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

quotelen = len(quotes) - 1

BOT_PREFIX = 'a-'
TOKEN = os_environ['BOT_TOKEN']

client = Bot(command_prefix = BOT_PREFIX)

# Bot is ready
@client.event
async def on_ready():
	print ("Starting up")
	await client.change_presence(game=discord.Game(name='| Type a-help for details!', type=1))
	print ("started")

# Test
@client.command()
async def test():
	await client.say("pong")

# Quote command
@client.command(pass_context = True)
async def quote(ctx, number: int = None):
	quotelen = len(quotes) - 1
	if number is None:
		quchoice = random.randint(0, quotelen)
	else:
		quchoice = number
	em = discord.Embed(title="Athel Quote", description=quotes[quchoice], color=0x00ffff)
	em.set_footer(text= "Quote #" + str(quchoice) + " of " + str(quotelen) + " quotes.")
	await client.send_message(ctx.message.channel, embed=em)

# Delete quote command
@client.command(pass_context = True)
async def delquote(ctx, number: int = None):
	if number is None:
		await client.say('You have to specify what quote to delete! Ex. a-delquote 2')
	else:
		quotes.pop(number)
		quotelen = len(quotes) - 1
		await client.say('Quote ' + str(number) + ' deleted!')

# Add quote command
@client.command(pass_context = True)
async def addquote(ctx, *, quadd: str = None):
	quotelen = len(quotes) - 1
	if quadd is None:
		await client.say('You have to type what the quote is in order to add it!')
	else:
		quotes.append(str(quadd))
		quotelen = len(quotes) - 1
		em = discord.Embed(title="Added quote", description=quadd, color=0x00ffff)
		em.set_footer(text=str(quotelen) + " quotes stored.")
		await client.send_message(ctx.message.channel, embed=em)
# Run bot
client.run(TOKEN)

if os.path.exists("athelbotcfg.txt"):
	os.remove("athelbotcfg.txt")

f = open("athelbotcfg.txt", "w+")

for item in quotes:
	f.write("%s\n" % item);
	
f.close()
print("configs saved");

print("The bot has been terminated.")
