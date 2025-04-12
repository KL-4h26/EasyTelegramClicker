from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from config import config_data
from components.buttons import *

router = Router()

@router.message(Command('start'))
async def start_command(message: Message):
    await message.answer(config_data["messages"]["start_message"], reply_markup=start_menu)
