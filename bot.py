import discord
from discord.ext import commands
import asyncio
import os


#GIVE YOUR BOT A PREFIX; mine is a.
bot = commands.Bot(command_prefix="^")




#PRINT THE DISCORD BOT'S NAME WHEN IT'S READY
@bot.event
async def on_ready():
  print(bot.user.name)

  
#A SIMPLE TEST COMMAND
@bot.command(pass_context=True)
async def hi(ctx):
  await bot.say("Hello there"+" "+ctx.message.author.name)
  
@bot.command(pass_context=True)
async def welcome(ctx):
  await bot.say("☆Welcome to my first Noob Bot☆"+" "+ctx.message.author.name)
  
@bot.command(pass_context=True)
async def goodmorning(ctx):
  await bot.say("Hey  hey!! goodmorning. 😎 Todays the perfect day to go to a beach😎😎."+" "+ctx.message.author.name)
 
@bot.command(pass_context=True)
async def goodnight(ctx):
  await bot.say("Now sleep quietly dont make any noises... Cause am sleeping right next to you!🤡"+" "+ctx.message.author.name)
  
@bot.command(pass_context=True)
async def goodday(ctx):
  await bot.say("Shit! Cause am having a bad day!😑"+" "+ctx.message.author.name)

@bot.command(pass_context=True)
async def why(ctx):
  await bot.say("I dont know man. Am so sad 😢😭"+" "+ctx.message.author.name)
  
@bot.command(pass_context=True)
async def who(ctx):
  await bot.say("Oh never mind 😔 it s just dyno 😝"+" "+ctx.message.author.name) 
  
@bot.command(pass_context=True)
async def thanks(ctx):
  await bot.say("No need to thank me bro. Am always here for you.😉"+" "+ctx.message.author.name)
  
@bot.command(pass_context=True)
async def talk(ctx):
  await bot.say("Nothing much just doing a  job for my girlfriend😎🤗 So please stop DISTURBING ME!!!!!"+" "+ctx.message.author.name) 
  
  
#YOU CAN USE os.environ TO HIDE YOUR BOT TOKEN: SAVE YOUR BOT TOKEN AS THE NAME YOU GAVE IN os.environ['name'] 
bot.run(os.environ['BOT_TOKEN'])
