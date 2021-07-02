# bot.py

import os
import discord
from dotenv import load_dotenv

from commands.echo import *
from commands.shuffle import *

load_dotenv()

token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')
prefix = os.getenv('COMMAND_PREFIX')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.display_name} has connected to {client.guilds[0].name}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    else:
        if message.content[0] == prefix:
            # $echo
            if message.content.split(' ')[0][1:] == 'echo':
                await message.channel.send(echo())

            # $shuffle
            if message.content.split(' ')[0][1:] == 'shuffle':
                await message.channel.send(shuffle())

client.run(token)