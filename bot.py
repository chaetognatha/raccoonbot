# bot.py
import os
import discord
from dotenv import load_dotenv # to load api key and keep code neat
from translate import from_spanish # the translation api is handled in a module

load_dotenv()
# so you need a text file named .env which declares the environment variable that comes next
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
	# this bit keeps the bot from reading it's own messages
	if message.author == client.user:
		return

	if message.content:
		# if there is a message, check if that message identifies as spanish
		response = from_spanish(message.content)
		if response:
			# the from_spanish() returns False for not Spanish
			await message.channel.send(response)

# RUN
client.run(TOKEN)
