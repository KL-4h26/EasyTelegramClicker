from aiogram import Bot, Dispatcher
from components.handlers import router
from config import config_data
import asyncio

bot = Bot(token=config_data["token"])
dp = Dispatcher()

async def start_bot():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start_bot())
