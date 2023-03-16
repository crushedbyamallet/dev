import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as dt

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('get in losers')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('alone on a saturday night? god, you are pathetic.'))
    print('get in losers')
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

@bot.command(pass_context=True)
async def asuka(ctx):
    await ctx.send('https://imgur.com/a/63GIoAJ')

@bot.command(pass_context=True)
async def therapy(ctx):
    await ctx.send('https://imgur.com/a/U4o0mY0')

@bot.command(pass_context=True)
async def saturday(ctx):
    await ctx.send('alone on a saturday night? god, you are pathetic.')

@bot.command(pass_context=True)
async def osdeverdade(ctx):
    await ctx.send('https://imgur.com/a/jM0PfvE')

bot.run('ODMxMDA5MjMzOTI3MDEyMzgz.YHO_qA.pIyMvRf7TaLVUDfksy8rgqHChEg')