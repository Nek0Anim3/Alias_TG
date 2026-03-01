
import asyncio
import db
from bot.connectBot import connectTGBot


async def main():
    await db.connect_Db()
    await connectTGBot()
    # await addPack(input("Тестовое имя записи: "))
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopped")
    

