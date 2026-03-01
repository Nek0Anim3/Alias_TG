from aiogram import Router, types, F, Bot
import db.lobbyHandle as dbLobby
from bot.keyboards.lobbies_list_board import lobbies_list_kb
from bot.handlers.start import main_menu
from bot.menus.LobbyMenu import lobby_menu
import asyncio

from db.userHandle import removePlayerfromDB

router = Router()

@router.callback_query(F.data == "create_lobby")
async def createLobby(callback: types.CallbackQuery):
    await dbLobby.createLobbyDB(callback.from_user.id, callback.from_user.full_name)
    await lobby_menu(callback.from_user.id, callback)


@router.callback_query(F.data == "list_lobby")
async def lobbiesList(callback: types.CallbackQuery):
    lobbies = await dbLobby.fetchLobbiesList()
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
    await asyncio.gather(dbLobby.deleteLobbyDB(uid, name), removePlayerfromDB(uid) ,main_menu(None, callback))

@router.callback_query(F.data.startswith("join_lobby:"))#LobbyCallback.filter(F.data == "join"))
async def joinLobby(callback: types.CallbackQuery):
    print("Joining lobby...")
    
    lobby_id = int(callback.data.split(":")[1])
    user_id = callback.from_user.id
    print("Lobby_ID In joinLobby, ", lobby_id)

    await dbLobby.joinLobbyDB(lobby_id , user_id, callback.from_user.full_name)
    await lobby_menu(lobby_id, callback)