import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re
bot = commands.Bot(command_prefix='>', description="bot de ayuda")

@bot.command()
async def ping(ctx):
    await ctx.send('eres un amor de persona')


@bot.command()
async def gaby(ctx):
    await ctx.send('silvi,es un loli,toda plana ')

@bot.command()
async def rules(ctx):
    await ctx.send('Prohibido el spam, pornografía o cualquiera otra cosa sin permiso.\n No xenofobia, machismo, hembrismo, homofobia, transfobia ni racismo. Tampoco insultos, provocaciones o faltas de respeto \n No bullying ni lenguaje ofensivo \n  Asegúrate de que todos se sientan seguros. No se permite el bullying ni los comentarios degradantes sobre la raza, la religión, la cultura, la orientación sexual, el sexo o la identidad')
@bot.command()
async def hola(ctx):
    await ctx.send('como estas 7u7')


@bot.command()
async def erick(ctx):
    await ctx.send('es gay')



@bot.command()
async def sum(ctx, numero1: int, numero2: int):
    await ctx.send(numero1 + numero2)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)
# Events

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="anime",url="https://www.twitch.tv/charlycharlie"))
    print('my bot es ta listo')

bot.run('NzU0MDEzNTI3MzAzNTIwMzc4.X1uj0Q.ErXXncwP_7v35gwdHBRGHKJBJHc')