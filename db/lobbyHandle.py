import asyncio

from db import get_Db
from db.userHandle import addPlayertoDB


async def createLobbyDB(uid: int, name: str):
    db = get_Db()
    col = db.get_collection('lobbys')
    await asyncio.gather(
        col.insert_one({
            "host": uid,
            "name": name,
            "status": "waiting",
            "players": [uid],
            "pack": "none"
        }),
        addPlayertoDB(uid, name, uid, "host")
    )

#-------------------------------

async def deleteLobbyDB(uid: int, name: str):
    db = get_Db()
    col = db.get_collection('lobbys')
    rmdoc = await col.find_one_and_delete({"host": uid})
    try:
        lobbies_id_list.remove(uid)
        lobbies_list.remove(name)
    except ValueError:
        pass
    print("Removed ", rmdoc)



lobbies_id_list = []
lobbies_list = []
async def fetchLobbiesList():
    global lobbies_id_list
    global lobbies_list 
    lobbies_id_list = []
    lobbies_list = []
    db = get_Db()
    col = db.get_collection('lobbys')
    
    lobbys_list = col.find({"status": "waiting"}).limit(10)
    async for lobby in lobbys_list: 
        if lobby["name"] in lobbies_list:
            continue
        else:
            lobbies_list.append(lobby["name"])
        #---------------------------------------
        if lobby["host"] in lobbies_id_list:
            continue
        else:
            lobbies_id_list.append([lobby["host"]])
        
    print("Lobby of players ", lobbies_list)
    print("IDs ", lobbies_id_list)
    return lobbies_list

async def findHostLobby():
    db = get_Db()
    # col.find

def getLobbyIdList():
    return lobbies_id_list


async def joinLobbyDB(lobby_id: int, user_id: int, usname: str):
    db = get_Db()
    col = db.get_collection('lobbys')
    print("Got lobby_id,", type(lobby_id))
    col.find_one_and_update({"host": lobby_id}, {'$push': {"players": user_id}})
    await addPlayertoDB(user_id, usname, lobby_id, "player")
    print("Added ", user_id)