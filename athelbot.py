from boto.s3.connection import S3Connection

import os

import discord
import random

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
print (quotelen)

SPACE_MAGIC = S3Connection(os.environ['SECRET_CODE_THING'])

client = discord.Client()
activity = discord.Game(name="with the API")

@client.event
async def on_message(message):
	quotelen = len(quotes) - 1
	if message.author == client.user:
		return
	
	if message.content.startswith('a-quote'): # Send a random quote
		quchoice = random.randint(0, quotelen)
		embed = discord.Embed(title="Athel Quote", description=quotes[quchoice], color=0x00ffff)
		embed.set_footer(text= "Quote #" + str(quchoice) + " of " + str(quotelen) + " quotes.")
		# msg = str(random.choice(quotes)).format(message)
		await client.send_message(message.channel, embed=embed)
	
	if message.content.startswith('a-embedtest'): # Testing how to do embeds
		embed = discord.Embed(title="Title", description="Desc", color=0x00ff00)
		embed.add_field(name="Field1", value="test", inline=False)
		embed.add_field(name="Field2", value=str(random.choice(quotes)), inline=False)
		embed.set_footer(text="testfooter")
		await client.send_message(message.channel, embed=embed)
		
	if message.content.startswith('a-help'): # Help command
		embed = discord.Embed(title="AthelBot commands", description="All command prefixes are 'a-', keep this in mind.", color=0x00ffff)
		embed.add_field(name="help", value="Displays this help dialogue.", inline=False)
		embed.add_field(name="quote", value="Picks a random Athel quote.", inline=False)
		embed.add_field(name="addquote", value="Add a quote to Athel quotes.", inline=False)
		embed.add_field(name="qnum", value="Pick a quote by number.", inline=False)
		await client.send_message(message.channel, embed=embed)
		
	if message.content.startswith('a-addquote'): # Add a quote
		msg = 'Please type the quote you want to add.'.format(message)
		print ("asked message")
		await client.send_message(message.channel, msg)
		msg = await client.wait_for_message(author=message.author)
		quotes.append(str(msg.content))
		print (quotes)
		msg = 'Quote added! ' + str(msg.content)
		quotelen = len(quotes)
		await client.send_message(message.channel, msg)
		
	if message.content.startswith('a-qnum'): # Add a quote
		msg = 'This is a WIP.'
		msg = 'Please select a quote (0 -' + str(len(quotes)-1) + ')'
		await client.send_message(message.channel, msg)
		msg = await client.wait_for_message(author=message.author)
		msg = str(msg.content)
		quchoice = int(msg.content)
		embed = discord.Embed(title="Athel Quote", description=quotes[quchoice], color=0x00ffff)
		embed.set_footer(text= "Quote #" + str(quchoice) + " of " + str(quotelen) + " quotes.")
		# msg = str(random.choice(quotes)).format(message)
		await client.send_message(message.channel, embed=embed)
		

		
@client.event
async def on_ready():

	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	
client.run(SPACE_MAGIC)

if os.path.exists("athelbotcfg.txt"):
	os.remove("athelbotcfg.txt")

f = open("athelbotcfg.txt", "w+")

for item in quotes:
	f.write("%s\n" % item);
	
f.close()
print("configs saved");
