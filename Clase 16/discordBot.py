import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'✅ Acabo de logearme cómo: {bot.user}')


async def comentar(comentario):
    channel = await bot.fetch_channel('1141489010057945211')
    await channel.send(comentario)


async def interacciones(interaccion):
    channel = await bot.fetch_channel('1141489151292747936')
    await channel.send(interaccion)


async def follow(usuario):
    channel = await bot.fetch_channel('1141489191637749891')
    await channel.send(usuario)

if __name__ == "__main__":
    bot.run(token)
