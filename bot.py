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
  await bot.say("☆Welcome to my first Lite Bot☆"+" "+ctx.message.author.name)
  
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
  
@bot.command(pass_context=True)
async def sing(ctx):
  await bot.say("Kiki, do you love me? Are you riding? Say you ll never ever leave from beside me Cause I want ya, and I need ya And I am down for you always KB, do you love me? Are you riding? Say you ll never ever leave from beside me Cause I want ya, and I need ya And I am down for you always"+" "+ctx.message.author.name)
 
@bot.command(pass_context=True)
async def seriously(ctx):
  await bot.say("Noo I was just kidding!! 😝 Am sorry honey I like him very much!😃"+" "+ctx.message.author.name)
  
@bot.command(pass_context=True)
async def revive(ctx):
  await bot.say("I mma kick your ass so hard that you ll be back to life 🙃😉"+" "+ctx.message.author.name)
 
@bot.command(pass_context=True)
async def pat(ctx):
  await bot.say("Thanks for patting me. You make me Happy 😄."+" "+ctx.message.author.name)
  
@bot.command(pass_context=True)
async def kill(ctx):
  await bot.say("Your wish shall be granted!!!! That Your daddy even wont know😈. I ll see you while you sleep FOREVER!!!!"+" "+ctx.message.author.name)

@bot.command(pass_context=True)
async def badday(ctx):
  await bot.say("Hehe... cause Am having a good day😂"+" "+ctx.message.author.name)
  
@bot.command(pass_context=True)
async def sup(ctx):
  await bot.say("▪We Will Contact  @Nøøb Gamer#3762 Sum More Information For This Bot.▪ "+" "+ctx.message.author.name)

  
#YOU CAN USE os.environ TO HIDE YOUR BOT TOKEN: SAVE YOUR BOT TOKEN AS THE NAME YOU GAVE IN os.environ['name'] 
bot.run(os.environ['BOT_TOKEN'])
