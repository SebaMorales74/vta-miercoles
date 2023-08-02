import discord
from discord.ext import commands
import datetime

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$',intents=intents)

@client.event
async def on_ready():
    print(f'✅ Acabo de logearme cómo: {client.user}')

@client.event
async def on_message(ctx):
    if ctx.author == client.user:
        return

    if ctx.content.startswith('$hora'):
        await ctx.channel.send(f'La hora es {datetime.datetime.now().time()}')

    if ctx.content.startswith('$video'):
        await ctx.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUJcmljayByb2xs')
    
    if ctx.content.startswith('123pormi'):
        connected = ctx.author.voice
        if not connected:
            await ctx.send("You need to be connected in a voice channel to use this command!")
            return
        global vc
        vc = await connected.channel.connect()

@client.command(name='join')
async def enter(ctx):
    print("Entre")
    connected = ctx.author.voice
    if not connected:
        await ctx.send("You need to be connected in a voice channel to use this command!")
        return
    global vc
    vc = await connected.channel.connect()

client.run('MTEzNjQxODI4NzE0MDQ4MzIwMw.GKiyQo.HOFIBeI0BXTFDOkLl_cich6VBHuC0S1c9yNEQY')
