import discord
import os
from discord.ext import commands
from discord.utils import get 

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)


@client.event
async def on_message(message):

    shrineChannel = client.get_channel(1054278583872401488)

    if message.content != '!pray' and message.channel == shrineChannel:
        print("Hello world")
    
client.run('MTAwOTU2NzA4NzU4NjQ1NTY0Mg.Gm-eqt.vYxr3oTXcPZQY5EXfgg3VOruti8kF6HwaII5Gs')