import discord

from bot.states.states import set_state

class LobbyMenuView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Створити лобі", style=discord.ButtonStyle.success)
    async def create_lobby(self, button: discord.ui.Button, interaction: discord.Interaction):
        await  interaction.edit_original_response(
            content="Введіть назву лобі",
            view=None
        )
        set_state(interaction.user.id, "lobby_name_input")

    @discord.ui.button(label="Назад", style=discord.ButtonStyle.secondary)
    async def back(self, button: discord.ui.Button, interaction: discord.Interaction):
        from bot.views.main_menu import MainMenu
        await interaction.edit_original_response(
            content="Меню лобі",
            view=MainMenu()
        )