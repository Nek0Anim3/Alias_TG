import discord
from discord import app_commands
from discord.ext import commands
from bot.views.main_menu import MainMenu

class MenuCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @app_commands.command(name="start", description="Відкриває стартове меню Еліас")
    async def start_menu(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "Вітаю в Alias",
            view=MainMenu(),
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(MenuCog(bot))