from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from config import config_data
from components.buttons import *
import aiosqlite

router = Router()

@router.message(Command('start'))
async def start_command(message: Message):
    await message.answer(config_data["messages"]["start_message"], reply_markup=start_menu)

# Главное меню

@router.callback_query(F.data == "click_menu")
async def click_menu(callback_query: CallbackQuery):
    await callback_query.message.edit_text(config_data["messages"]["click_message"], reply_markup=click_keboard)

@router.callback_query(F.data == "stats")
async def click_menu(callback_query: CallbackQuery):
    async with aiosqlite.connect(config_data["path_to_db"]) as db:
        cursor = await db.execute(f"SELECT id, balance FROM users WHERE id = {callback_query.message.from_user.id}")
        data = await cursor.fetchone()

    await callback_query.message.edit_text(f"""
📊 Статистика кликов

id: {callback_query.message.from_user.id}
Клики: {data[1] / config_data["click_reward"] if data else 0}
Монеты: {data[1] if data else 0}
""", reply_markup=stats_menu)

@router.callback_query(F.data == "shop")
async def click_menu(callback_query: CallbackQuery):
    await callback_query.message.edit_text("Ну типо перешел в магаз")

# Click-menu callbacks
@router.callback_query(F.data == "click")
async def click(callback_query: CallbackQuery):

    async with aiosqlite.connect(config_data["path_to_db"]) as db:
        cursor = await db.execute("SELECT id, balance FROM users WHERE id = ?", (callback_query.message.from_user.id,))
        data = await cursor.fetchone()

        if data:
            await db.execute(f"UPDATE users SET balance = {data[1] + config_data["click_reward"]} WHERE id = {callback_query.message.from_user.id};")

        else:
            await db.execute("INSERT INTO users (id, balance) VALUES (?, ?)", (callback_query.message.from_user.id, config_data["click_reward"]))

        await db.commit()

    await callback_query.answer("+ 5 монет")


# Back Callback
@router.callback_query(F.data == "back")
async def back_to_menu(callback_query: CallbackQuery):
    await callback_query.message.edit_text(config_data["messages"]["start_message"], reply_markup=start_menu)
