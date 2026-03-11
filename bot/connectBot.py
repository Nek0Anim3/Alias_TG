import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())
async def start_bot():
    async with bot:
        await bot.load_extension("bot.cogs.main_menu_cog")
        await bot.start(os.getenv("BOT"))

# @bot.event
# async def on_ready():
#     await bot.tree.sync()
