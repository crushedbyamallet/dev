import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as dt
import youtube_dl 
from youtube_dl import YoutubeDL
from music_cog import music_cog

bot = commands.Bot(command_prefix='!')

bot.add_cog(music_cog(bot))

@bot.event
async def on_ready():
    print('get in losers')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('alone on a saturday night? god, you are pathetic.'))
    print('get in losers')
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

@bot.command()
async def userinfo(ctx, member: discord.Member):

    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    
    embed.set_author(name=f"user info - {member}")

    embed.set_thumbnail(url=member.avatar_url)

    embed.set_footer(text=f"requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID:", value=member.id)

    embed.add_field(name="server's name:", value=member.display_name)

    embed.add_field(name="created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    
    embed.add_field(name="joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name=f"roles ({len(roles)})", value=" ".join([role.mention for role in roles]))


    await ctx.send(embed=embed)


@bot.command()
async def server(ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)
        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(   
            title=name + " server info ",
            description= description,
            color=discord.Color.red()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="owner", value=owner, inline=True)
        embed.add_field(name="server ID", value=id, inline=True)
        embed.add_field(name="region", value=region, inline=True)
        embed.add_field(name="member count", value=memberCount, inline=True)

        await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("connect to a voice channel before you dumb dumb ")

@bot.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("bye fucker")
    else:
        await ctx.send("im not in a voice channel you dumb dumb")

@bot.command(pass_context=True)
async def asuka(ctx):
    await ctx.send('https://imgur.com/a/63GIoAJ')

@bot.command(pass_context=True)
async def therapy(ctx):
    await ctx.send('https://imgur.com/a/U4o0mY0')

@bot.command(pass_context=True)
async def lmfao(ctx):
    await ctx.send('lmfao')
    await ctx.send('https://imgur.com/a/joMWShx')
  
@bot.command(pass_context=True)
async def saturday(ctx):
    await ctx.send('alone on a saturday night? god, you are pathetic.')

@bot.command(pass_context=True)
async def osdeverdade(ctx):
    await ctx.send('https://imgur.com/a/jM0PfvE')

@bot.command(pass_context=True)
async def luke(ctx):
    await ctx.send('aqui esta o luke festa')
    await ctx.send('https://imgur.com/a/KEgL6Mt')

@bot.command(pass_context=True)
async def bd(ctx):
    await ctx.send('bOM dia')
    await ctx.send('https://imgur.com/uFtZSbU')

@bot.command(pass_context=True)
async def jantapoli(ctx):
    await ctx.send('rodelas')
    await ctx.send('https://imgur.com/a/LxpSwkI')

@bot.command(pass_context=True)
async def lipe(ctx):
    await ctx.send('felipe holanda')
    await ctx.send('https://imgur.com/a/7MtlQ4v') 

@bot.command(pass_context=True)
async def calebe(ctx):
    await ctx.send('careca')
    await ctx.send('https://imgur.com/a/ONyVMI2') 

@bot.command(pass_context=True)
async def fn(ctx):
    await ctx.send('watch out for the friday night gang')
    await ctx.send('https://imgur.com/a/dFJRvi1') 

@bot.command(pass_context=True)
async def amongus(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/687930213229002778/813943500071895090/video0.mp4') 

@bot.command(pass_context=True)
async def monday(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/830986740562132992/831112255000150056/rise_and_shine.mp4') 

@bot.command(pass_context=True)
async def googas(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/735602075064336529/829496997588631562/googas.mp4') 

@bot.command(pass_context=True)
async def ow(ctx):
    await ctx.send('ow rapaziada vo de berço aqui')

bot.run('ODMxMDA5MjMzOTI3MDEyMzgz.YHO_qA.pIyMvRf7TaLVUDfksy8rgqHChEg')  