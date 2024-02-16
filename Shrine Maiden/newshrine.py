import discord
from discord.ext import commands
from discord_slash import SlashCommand
import random

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

client = commands.Bot(command_prefix = '!')
slash = SlashCommand(client, sync_commands = True)


#@client.event
#async def on_ready():
  #print("Hello world")
  #welcomeChannel = client.get_channel(1009334579468976229)

# embed = embed = discord.Embed( #Rules
#title = "Welcome to the Guuji Gang", # add more to this line of code
#description = f"welcome to my server! This is a server for my close friends, friends, and followers of youtube, twitch, etc. I give tips for VALORANT and Genshin Impact mostly, not really anything else. If you need people to talk to , just talk to us. It would be so chill ngl", # add more on to this line of code
#color = 0xffb7c5
# )
#embed.add_field(
#name = "Please follow these simple rules: (made by Justin)",
#value = "1. be nice to everyone in the server, don't be a jerk\n\n 2. no inappropiate content unless you are the channels that are meant for that stuff\n\n 3. be chill",
#inline = True
#)
# embed.set_image(url = 'https://media.tenor.com/l4W3705N6FwAAAAd/yae-miko.gif')
#await welcomeChannel.send(embed = embed

@client.slash_command()
async def hello(ctx):
  await ctx.send(f"Hello {ctx.author.mention}!")
  












@client.event
async def on_message(message):

  shrineChannel = client.get_channel(1054278583872401488)
  if message.content == '!pray':
    embed = embed = discord.Embed(
      title="Prayer Completed!",
      description="Your prayer has been made to the Narukami Shrine!",
      color=0xffb7c5)
    embed.set_thumbnail(
      url=
      'https://images.unsplash.com/photo-1598957232485-fab51e0ed7e8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8c2FrdXJhJTIwdHJlZXxlbnwwfHwwfHw%3D&w=1000&q=80'
    )
    embed.set_image(
      url=
      'https://preview.redd.it/805k2fahs5b81.jpg?auto=webp&s=61487a52871b488518202c3eff63b6a59a69d922'
    )
    await shrineChannel.send(embed=embed)


@client.event
async def on_member_join(member):
  embed = embed = discord.Embed(
    title="Welcome to our server!",
    description=
    "\nWelcome to the Guuji Gang Discord, the discord of Justin and Friends!\n\n For any questions on what we do in the discord or any other stuff, look in the information category of our discord to learn more about our rules, roles, and all the channels found in the discord. Hope you have a good time!",
    color=0xffb7c5)
  embed.set_image(url='https://media.tenor.com/WOI-Uykj-9kAAAAC/yae-miko.gif')
  await member.send(embed=embed)

  guild = client.get_guild(892558253790199819)
  mainchat = guild.get_channel(1054268892958179328)
  await mainchat.send(f'Welcome to the server {member.name} !')

  memberRole = guild.get_role(1009670274741960744)
  await member.add_roles(memberRole, atomic=True)


keep_alive()
client.run(
  'MTAwOTU2NzA4NzU4NjQ1NTY0Mg.Gm-eqt.vYxr3oTXcPZQY5EXfgg3VOruti8kF6HwaII5Gs')
