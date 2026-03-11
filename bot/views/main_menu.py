import discord


class MainMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(style=discord.ButtonStyle.primary, label="Лобі", custom_id='open_lobby')
    async def open_lobby(self, interaction: discord.Interaction, button: discord.ui.Button):
        from bot.views.lobby_menu import LobbyMenuView
        await interaction.edit_original_response(
            content="Меню лобі",
            view=LobbyMenuView()
        )


