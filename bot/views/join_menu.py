from bot.views.base import BaseView

class JoinMenuView(BaseView):
    menu_text = "Підключення до лобі.. \nВведіть код лобі"

    def __init__(self):
        from bot.views.main_menu import MainMenuView
        super().__init__(back_view=MainMenuView)
