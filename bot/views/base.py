#базовий клас для менюшок, щоб не прописувати кожен раз шаблон
import discord

class BaseView(discord.ui.View):
    menu_text = "Меню"
    def __init__(self, back_view: "BaseView" = None, timeout=None):
        super().__init__(timeout=timeout)
        if back_view is not None:
            self.add_item(BackButton(back_view))

    async def goto(self, interaction: discord.Interaction, view: "BaseView"):
        await interaction.response.edit_message(
            content=view.menu_text,
            view=view
        )

class BackButton(discord.ui.Button):
    def __init__(self, target_view: "BaseView"):
        super().__init__(
            label="Назад",
            style=discord.ButtonStyle.secondary,
            row=4
        )
        self.target_view = target_view

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.edit_message(
            content=self.target_view.menu_text,
            view=self.target_view
        )