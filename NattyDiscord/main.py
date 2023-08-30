import discord
from discord.ext import commands

import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="¿",intents=intents)

@bot.event
async def on_ready():
    print(f"🐝 NattyDiscord está en funcionamiento. ID del bot: {bot.user}")

@bot.event
async def on_message(ctx):
    return

if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except:
        print("Hubo un error al iniciar el bot 😪")