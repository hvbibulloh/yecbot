from aiogram import types

from keyboards.inline.katalog_inline import location_keyboard
from loader import dp, bot


@dp.message_handler(text="Боғланиш ☎️")
async def boglanish(message: types.Message):
    await message.answer(text="Biz bilan bog'lanish uchun telefon raqam:\n+998981309999",
                         reply_markup=location_keyboard)
    await bot.pin_chat_message(chat_id=message.chat.id, message_id=message.message_id)


@dp.message_handler(text="Ижтимоий тармоқларимиз 📱")
async def tarmoq(message: types.Message):
    phone_number = "+998981309999"
    instagram_link = "https://www.instagram.com/luxgilam_carpet/"
    youtube_link = "https://youtube.com/@luxgilam7654"
    await message.answer(f"Оператор: <a href=\"tel:{phone_number}\">{phone_number}</a>\n"
                         f"<a href=\"{instagram_link}\">Instagram</a>\n"
                         f"<a href=\"{youtube_link}\">YouTube</a>\n"
                         f"@LuxGilam_rasmiy", parse_mode="HTML")
