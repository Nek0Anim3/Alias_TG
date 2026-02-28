from aiogram import Router, types, F, Bot
from db.lobbyHandle import createLobbyDB, fetchLobbiesList, deleteLobbyDB, joinLobbyDB
from bot.keyboards.lobbies_list_board import lobbies_list_kb
from bot.handlers.start import main_menu
from bot.callbacks.lobby import LobbyCallback

router = Router()

@router.callback_query(F.data == "create_lobby")
async def createLobby(callback: types.CallbackQuery):
    print(callback.from_user.full_name)
    await createLobbyDB(callback.from_user.id, callback.from_user.full_name)

    await callback.message.edit_text(
        text="да да мгм", 
        reply_markup=types.InlineKeyboardMarkup(
        inline_keyboard=[[
            types.InlineKeyboardButton(text="Почати гру", callback_data="start_game"),
            types.InlineKeyboardButton(text="Налаштування", callback_data="settings")
        ],
        [
            types.InlineKeyboardButton(text="Обрати пак", callback_data="pack"),
            types.InlineKeyboardButton(text="Вийти", callback_data="quit_lobby")
        ]
        ]
    ))

@router.callback_query(F.data == "list_lobby")
async def lobbiesList(callback: types.CallbackQuery):
    lobbies = await fetchLobbiesList()
    keyboard = await lobbies_list_kb(lobbies)
    await callback.message.edit_text(
        text="Список лобі",
        reply_markup=keyboard.as_markup()
        #types.InlineKeyboardMarkup(
        #inline_keyboard=)
    )

@router.callback_query(F.data == "quit_lobby")
async def quitLobby(callback: types.CallbackQuery):
    uid = callback.from_user.id
    name = callback.from_user.full_name
    #if 
    await deleteLobbyDB(uid, name)
    await main_menu(None, callback)

@router.callback_query(F.data.startswith("join_lobby:"))#LobbyCallback.filter(F.data == "join"))
async def joinLobby(callback: types.CallbackQuery):
    print("Joining lobby...")
    
    #int()
    lobby_id = int(callback.data.split(":")[1])
    #на таких костылях даже мой дед не ходил после перелома

    #int()
    user_id = int(callback.from_user.id)
    print("Lobby_ID In joinLobby, ", lobby_id)


    #изгой общества снизу 👇👇👇👇👇👇👇

    await joinLobbyDB(lobby_id , user_id)
    
    #изгой общества сверху 👆👆👆👆👆👆
    #этот дурачoк думал что сможет типизировать в пайтон боже нищий
    
    await callback.message.edit_text(
        text="tipa connected",
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[[types.InlineKeyboardButton(text="Back", callback_data="start")]] 
        )
        #inline_keyboard=)
    )