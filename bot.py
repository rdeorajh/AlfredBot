import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import sys
import typing

#Alfred Classes
from alfred_speech import AlfredSpeech

myClient = commands.Bot(command_prefix=">")
alfredQuotes = AlfredSpeech()

@myClient.event
async def on_ready():
  print('Logged in as {0.user}'.format(myClient))

@myClient.event
async def on_command_error(ctx,error):
      await ctx.send("Forgive me. The Exalted One (Ryan Deorajh) has not programmed me for this yet. Is there any other way I can be of service?")


@myClient.command()
async def hi(ctx):
  await ctx.send('Good day, {0.author.display_name}. My name is Alfred. How may I be of service to you?'.format(ctx))
  return

@myClient.command()
async def inspire(ctx,arg: typing.Optional[discord.Member], _str = ""):
  if isinstance(arg,discord.Member):
    nameStr = "{0.display_name}, ".format(arg)
    await ctx.send(nameStr + alfredQuotes.compliment())
  elif _str == "me":
  	await ctx.send(alfredQuotes.compliment())
  elif _str == "us" or _str == "":
    await ctx.send(alfredQuotes.inspire())
  else:
    await ctx.send("Forgive me, I don't quite understand. Is there any other way I can be of service?")
    pass
  return



load_dotenv()
myClient.run(os.getenv('TOKEN'))