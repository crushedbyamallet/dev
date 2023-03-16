import discord

client = discord.Client()

client = commands.Bot(command_prefix = '=')

@client.event
async def on_ready():

    hm = client.get_channel(830986740562132992)

    await hm.send("get in losers, we are going to therapy")


@client.command()
async def asuka(ctx):
        await ctx.send('fuck off')


client.run('ODMwOTYzODIxNDU4ODgyNjAx.YHOVXQ.MEQP-j3NSnojNJ9FtF6AAQILn0k')