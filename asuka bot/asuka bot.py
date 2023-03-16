import discord 
from discord.ext import commands 

client = commands.Bot(command_prefix ='.')

@client.event 
async def on_ready():
    print('get in losers, we are going to therapy.')

    client.run('ODMwOTYzODIxNDU4ODgyNjAx.YHOVXQ.MEQP-j3NSnojNJ9FtF6AAQILn0k')