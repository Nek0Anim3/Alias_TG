from aiogram.types import CallbackQuery

from db import get_Db

async def addPlayertoDB(uid: int, usname: str, lobby_id: int, role: str):
    db = get_Db()
    col = db.get_collection("players")
    await col.insert_one({
        "uid": uid,
        "name": usname,
        "lobby_id": lobby_id,
        "role": role
    })
    print("Player added", uid)

async def removePlayerfromDB(uid: int):
    db = get_Db()
    col = db.get_collection("players")
    await col.find_one_and_delete({"uid": uid})
    print("Player deleted", uid)