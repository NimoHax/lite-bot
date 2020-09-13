import discord
from discord.ext import commands
import asyncio

TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx' # add your token here

#Send anonymous DM's
@client.command()
async def send_anonymous_dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm() # creates a DM channel for mentioned user
    await channel.send(content) # send whatever in the content to the mentioned user.
# Usage: !send_anonymous_dm @mention_user <your message here>

# THIS FUNCTION WILL SEND A DM WITH THE AUTHORS NAME.
@client.command()
async def sendDM(ctx, member: discord.Member, *, content):
    channel = await member.create_dm() # creates a DM channel for mentioned user
    await channel.send(f"**{ctx.message.author} said:** {content}") # send whatever in the content to the mentioned user along with the author's name.

# Usage: !send_anonymous_dm @mention_user <your message here>


client.run(TOKEN)
