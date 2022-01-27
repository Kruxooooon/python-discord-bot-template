import discord
from discord.ext import commands


client = commands.Bot(command_prefix="#") # In "" put your's prefix to bot, i set it to "#"
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot ready to work!")
    await client.change_presence(activity= discord.Game(name= "Under development - for example")) # Here you can put your activity   


client.run("TOKEN") # Put your's token here

#Important thing, before you run your's bot install discord.py in cmd
#pip install discord.py
