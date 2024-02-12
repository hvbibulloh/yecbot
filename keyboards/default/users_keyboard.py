from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db

users_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Бизнинг Каталог 📒")

        ],
        [
            KeyboardButton("Боғланиш ☎️")
        ],
        [
            KeyboardButton("Ижтимоий тармоқларимиз 📱")
        ]
    ], resize_keyboard=True
)


def category_button():
    categories = db.get_categories()
    btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
    orqaga = KeyboardButton("Chiqish")
    btn.add(orqaga)
    for i in categories:
        btn.add(f"{i[1]} 🔰")

    return btn


send_contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Contact', request_contact=True),
        ]
    ],
    resize_keyboard=True)
