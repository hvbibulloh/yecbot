from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging

from aiogram.utils.callback_data import CallbackData
from loader import db


async def category_keyboard():
    markup = InlineKeyboardMarkup(row_width=1)
    data = await db.get_categories()
    if data:
        for i in data:
            markup.add(InlineKeyboardButton(
                text=f"{i[1]} 🔰", callback_data=f"cat_{i[0]}"
            ))
    return markup


location_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Наманган вилоят филиал 📍", url="https://maps.app.goo.gl/V5qXk3jLsZDBsT316")
    ],
    [
        InlineKeyboardButton(text="Наманган шахар филиал 📍", url="https://maps.app.goo.gl/dyQSeNe8nuPjJwyv9")
    ],
    [
        InlineKeyboardButton(text="Андижон вилоят филиал 📍", url="https://maps.app.goo.gl/HUek9GP3E7gnBXoS8")
    ],
    [
        InlineKeyboardButton(text="Шахрихон шахар филиал 📍", url="https://maps.app.goo.gl/V6ZasS5jgAGAoZti8")
    ],
    [
        InlineKeyboardButton(text="Кукон шахар филиал 📍", url="https://maps.app.goo.gl/eRUCvVE7cqhJrtjB9")
    ],
    [
        InlineKeyboardButton(text="Кукон шахар филиал 📍", url="https://maps.app.goo.gl/KzJTQrEGJAEkNJwN6")
    ],
    [
        InlineKeyboardButton(text="Маргулон шахар филал 📍", url="https://maps.app.goo.gl/f5PVb5PonxydaCEb")
    ],
    [
        InlineKeyboardButton(text="Риштон шахар филиал 📍", url="https://maps.app.goo.gl/QVMRZBDnFLpKVBTw8")
    ]
])
