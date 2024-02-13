from aiogram import types

from keyboards.default.users_keyboard import users_keyboard
from loader import dp


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Aссалому алейкум {message.from_user.full_name}", reply_markup=users_keyboard)




