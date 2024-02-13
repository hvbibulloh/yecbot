from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.default.users_keyboard import send_contact, users_keyboard
from keyboards.inline.katalog_inline import category_keyboard
from loader import dp, db, BASE, bot


class BoglanishState(StatesGroup):
    phone = State()


@dp.message_handler(text="Бизнинг Каталог 📒")
async def bizning_katalog(message: types.Message):
    await message.answer(f"Ассалому алайкум {message.from_user.first_name}\nКеракли бўлим танланг ✅",
                         reply_markup=await category_keyboard())


@dp.callback_query_handler(lambda call: call.data.split('_')[0] == "cat")
async def inline_katalog_callback(call: types.CallbackQuery):
    id = call.data.split('_')[1]
    data = await db.get_sub_categories(int(id))
    if data:
        media = []
        for i in data:
            work = types.InlineKeyboardButton(text=f'{i[1]}', callback_data=f'sub_{i[0]}')
            btn_work = types.InlineKeyboardMarkup(inline_keyboard=[[work]])
            for j in i[2:6]:
                media.append(types.InputMediaPhoto(media=open(f"{BASE}/admin/media/{j}", 'rb')))
                if len(media) == 4:
                    await bot.send_media_group(chat_id=call.message.chat.id, media=media)
                    await call.message.answer(f"⚜ {i[1]} ⚜ Коллекцияси учун гиламлар", reply_markup=btn_work)
                    media = []
        if media:
            await bot.send_media_group(chat_id=call.message.chat.id, media=media)


@dp.callback_query_handler(lambda call: call.data.split('_')[0] == 'sub')
async def product_katalog_inline(call: types.CallbackQuery):
    id = call.data.split('_')[1]
    n = 1
    data = await db.get_product(int(id))
    if data and len(data) > 1:
        end = types.InlineKeyboardButton('🔙', callback_data=f'back_{len(data) if n == 1 else n - 1}_{id}')
        work = types.InlineKeyboardButton('Sotib Olish', callback_data=f'work_{n}_{id}_{data[n - 1][0]}')
        next = types.InlineKeyboardButton('🔜', callback_data=f'next_{1 if n == len(data) else n + 1}_{id}')
        btn = types.InlineKeyboardMarkup(inline_keyboard=[[end, work, next]])
        await call.message.answer_photo(photo=open(f"{BASE}/admin/media/{data[n - 1][2]}", 'rb'),
                                        caption=f"<b>Ишлаб чикарилиши:</b> {data[n - 1][3]}\n<b>Коллекция:</b> {data[n - 1][1]}\n<b>Стиль:</b> {data[n - 1][4]}\n<b>Ип тури:</b> {data[n - 1][6]}\n<b>Ворси баландлиги:</b> {data[n - 1][-1]}\n<b>Зичлиги:</b> {data[n - 1][9]}\n<b>Форма:</b> {data[n - 1][5]}\n<b>Ранглар:</b> {data[n - 1][10]}\n<b>Размер:</b> {data[n - 1][7]} x {data[n - 1][8]}\n<b>Нархи:</b> {data[n - 1][11] * data[n - 1][7] * data[n - 1][8]} сум\n",
                                        reply_markup=btn, parse_mode="HTML")


    elif data and len(data) == 1:
        work = types.InlineKeyboardButton('Sotib Olish', callback_data=f'work_{n}_{id}_{data[n - 1][0]}')
        btn_work = types.InlineKeyboardMarkup(inline_keyboard=[[work]])
        await call.message.answer_photo(photo=open(f"{BASE}/admin/media/{data[n - 1][2]}", 'rb'),
                                        caption=f"<b>Ишлаб чикарилиши:</b> {data[n - 1][3]}\n<b>Коллекция:</b> {data[n - 1][1]}\n<b>Стиль:</b> {data[n - 1][4]}\n<b>Ип тури:</b> {data[n - 1][6]}\n<b>Ворси баландлиги:</b> {data[n - 1][-1]}\n<b>Зичлиги:</b> {data[n - 1][9]}\n<b>Форма:</b> {data[n - 1][5]}\n<b>Ранглар:</b> {data[n - 1][10]}\n<b>Размер:</b> {data[n - 1][7]} x {data[n - 1][8]}\n<b>Нархи:</b> {data[n - 1][11] * data[n - 1][7] * data[n - 1][8]} сум\n"
                                        , reply_markup=btn_work, parse_mode="HTML")
    else:
        await call.message.answer(text='Hozircha Gilamlar mavjud emas!')


@dp.callback_query_handler(lambda callback: callback.data.split('_')[0] in ['back', 'work', 'next'])
async def callback_handler(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    id = callback.data.split('_')[2]
    stories = await db.get_product(int(id))
    n = 1
    text = callback.data.split('_')
    if text[0] == 'back':
        n = int(text[1])
    elif text[0] == 'work':
        index = int(callback.data.split('_')[3])
        async with state.proxy() as data:
            data['media_id'] = index
        await BoglanishState.phone.set()
        await callback.message.answer(text="Телефон рақамингизни юборинг ☎", reply_markup=send_contact)
        return
    elif text[0] == 'next':
        n = int(text[1])
    end = types.InlineKeyboardButton('🔙', callback_data=f'back_{len(stories) if n == 1 else n - 1}_{id}')
    work = types.InlineKeyboardButton('Sotib Olish', callback_data=f'work_{n}_{id}_{stories[n - 1][0]}')
    next = types.InlineKeyboardButton('🔜', callback_data=f'next_{1 if n == len(stories) else n + 1}_{id}')
    btn = types.InlineKeyboardMarkup(inline_keyboard=[[end, work, next]])
    await callback.message.answer_photo(photo=open(f"{BASE}/admin/media/{stories[n - 1][2]}", 'rb'),
                                        caption=f"<b>Ишлаб чикарилиши:</b> {stories[n - 1][3]}\n<b>Коллекция:</b> {stories[n - 1][1]}\n<b>Стиль:</b> {stories[n - 1][4]}\n<b>Ип тури:</b> {stories[n - 1][6]}\n<b>Ворси баландлиги:</b> {stories[n - 1][-1]}\n<b>Зичлиги:</b> {stories[n - 1][9]}\n<b>Форма:</b> {stories[n - 1][5]}\n<b>Ранглар:</b> {stories[n - 1][10]}\n<b>Размер:</b> {stories[n - 1][7]} x {stories[n - 1][8]}\n<b>Нархи:</b> {stories[n - 1][11] * stories[n - 1][7] * stories[n - 1][8]} сум\n"
                                        , reply_markup=btn, parse_mode="HTML")
    await callback.answer(str(f"📑 Siz shu sahifadasiz: {n}"))


@dp.message_handler(state=BoglanishState.phone, content_types=types.ContentType.CONTACT)
async def phone_handler(message: types.Message, state: FSMContext):
    await message.answer(
        "Телефон рақамингизни юборганингиз учун раҳмат!😊\n Тез орада операторларимиз сиз билан боғланишади 👩🏻‍💻",
        reply_markup=users_keyboard)
    async with state.proxy() as data:
        id = data['media_id']
        send = await db.get_products(int(id))
        for i in send:
            await bot.send_message(chat_id=941535008,
                                   text=f"Mijoz Telefon raqami: {message.contact.phone_number}\n\nXarid qilmoqchi 🤝:\n\nIshlab chiqarilishi: {i[3]}\nNomi: {i[1]}\nStill: {i[4]}\nIp turi {i[6]}\nVorsi {i[-1]}\nZichligi {i[9]}\nForma {i[5]}\nRazmer {i[7]} x {i[8]}\nNarxi {i[7] * i[8] * i[11]}")

    await state.finish()


@dp.message_handler(commands="start", state=BoglanishState.phone)
async def start_phone(message: types.Message, state: FSMContext):
    await message.answer("Bosh Menu 🏠", reply_markup=users_keyboard)
    await state.finish()
