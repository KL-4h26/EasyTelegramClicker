from aiogram import Bot, Dispatcher
from components.handlers import router
from config import config_data
import asyncio
import aiosqlite

bot = Bot(token=config_data["token"])
dp = Dispatcher()

async def start_bot():
    async with aiosqlite.connect(config_data["path_to_db"]) as db:
        await db.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER, balance INTEGER)")

    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start_bot())
