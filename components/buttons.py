from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="👾 Кликать 🪙", callback_data="click_menu")],
    [InlineKeyboardButton(text="📈 Статистика 📉", callback_data="stats"), InlineKeyboardButton(text="🛍️ Магазин 💸", callback_data="shop")]
])

click_keboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="➡️ Клик ⬅️", callback_data="click")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
])

stats_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
])
