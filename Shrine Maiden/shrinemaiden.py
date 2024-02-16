import discord
from discord import app_commands
import asyncio

class MyClient(discord.Client):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  
  async def on_ready(self):
    await tree.sync(guild = discord.Object(id = 892558253790199819))
    print("The bot is online. Hello world!")

client = MyClient(intents=discord.Intents.default())
tree = app_commands.CommandTree(client)

@tree.context_menu(name = "Hello", guild = discord.Object(id = 892558253790199819))

async def hello(interaction: discord.Interaction, message : discord.Message):
  await interaction.response.send_message("Hey!")


client.run('MTAwOTU2NzA4NzU4NjQ1NTY0Mg.Gm-eqt.vYxr3oTXcPZQY5EXfgg3VOruti8kF6HwaII5Gs')



