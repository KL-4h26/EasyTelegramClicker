from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="👾 Кликать 🪙", callback_data="click")],
    [InlineKeyboardButton(text="📈 Статистика 📉", callback_data="stats"), InlineKeyboardButton(text="🛍️ Магазин 💸", callback_data="shop")]
])
