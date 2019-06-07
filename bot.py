import discord
from discord.ext import commands
from discord.utils import get

client = discord.Client()
token = "NTgwNDEyNzI3OTk5MjAxMjkw.XPnRtg.qaEVdGMaPNyT-4l1l9UMLm6bSOg"

def check_valid(message):
    if message.content.find("ชื่อ") != -1:
        return True
    return False


def get_channel(channel_name):
    all_channels = client.get_all_channels()
    channelToBroadcast = None
    for channel in all_channels:
        if channel.name == channel_name and channel.type == ChannelType.text:
            channelToBroadcast = channel
    return channelToBroadcast


def get_role(role_name, server):
    for role in server.roles:
        if role.name == role_name:
            return role
    return None

# --------------------------------------------------------------------------------------------------------------

@client.event
async def on_message(message):
    if message.author.bot == True or len(message.content) <= len("ชื่อ") or str(message.channel) != "welcome_room": 
        return
    if check_valid(message):
        role = discord.utils.get(message.guild.roles, name="Checked")
        await message.author.add_roles(role)
    

# --------------------------------------------------------------------------------------------------------------

client.run(token)
