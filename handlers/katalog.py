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
async def inline_katalog_callback(call: types.CallbackQuery, state: FSMContext):
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

    else:
        await call.message.answer("Gilamlar mavjud emas ⛔")


@dp.callback_query_handler(lambda call: call.data.split('_')[0] == 'sub')
async def product_katalog_inline(call: types.CallbackQuery, state: FSMContext):
    id = call.data.split('_')[1]
    sub_data = await db.get_products_sub(int(id))

    n = 1
    data = await db.get_product(int(id))


    if data and len(data) > 1:
        end = types.InlineKeyboardButton('🔙', callback_data=f'back_{len(data) if n == 1 else n - 1}_{id}')
        work = types.InlineKeyboardButton('Sotib Olish', callback_data=f'work_{n}_{id}_{data[n - 1][0]}')
        next = types.InlineKeyboardButton('🔜', callback_data=f'next_{1 if n == len(data) else n + 1}_{id}')
        btn = types.InlineKeyboardMarkup(inline_keyboard=[[end, work, next]])
        if data[n - 1][-1] == True:
            await call.message.answer_photo(photo=open(f"{BASE}/admin/media/{data[n - 1][1]}", 'rb'),
                                            caption=f"<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {data[n - 1][2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {data[n - 1][3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {data[n - 1][4]} x {data[n - 1][5]}\n<b>Нархи:</b> {data[n - 1][4] * data[n - 1][5] * sub_data[-2]} сум\n\nНасия Савдо Мавжуд ✅",
                                            reply_markup=btn, parse_mode="HTML")
        elif data[n - 1][-1] == False:
            await call.message.answer_photo(photo=open(f"{BASE}/admin/media/{data[n - 1][1]}", 'rb'),
                                            caption=f"<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {data[n - 1][2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {data[n - 1][3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {data[n - 1][4]} x {data[n - 1][5]}\n<b>Нархи:</b> {data[n - 1][4] * data[n - 1][5] * sub_data[-2]} сум\n\nНасия Савдо Мавжуд Емас ❌",
                                            reply_markup=btn, parse_mode="HTML")


    elif data and len(data) == 1:
        work = types.InlineKeyboardButton('Sotib Olish', callback_data=f'work_{n}_{id}_{data[n - 1][0]}')
        btn_work = types.InlineKeyboardMarkup(inline_keyboard=[[work]])

        if data[n - 1][-1] == True:
            await call.message.answer_photo(photo=open(f"{BASE}/admin/media/{data[n - 1][1]}", 'rb'),
                                            caption=f"<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {data[n - 1][2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {data[n - 1][3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {data[n - 1][4]} x {data[n - 1][5]}\n<b>Нархи:</b> {data[n - 1][4] * data[n - 1][5] * sub_data[-2]} сум\n\nНасия Савдо Мавжуд ✅"

                                            , reply_markup=btn_work, parse_mode="HTML")

        elif sub_data[n - 1][-1] == False:
            await call.message.answer_photo(photo=open(f"{BASE}/admin/media/{data[n - 1][1]}", 'rb'),
                                            caption=f"<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {data[n - 1][2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {data[n - 1][3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {data[n - 1][4]} x {data[n - 1][5]}\n<b>Нархи:</b> {data[n - 1][4] * data[n - 1][5] * sub_data[-2]} сум\n\nНасия Савдо Мавжуд Емас ❌"

                                            , reply_markup=btn_work, parse_mode="HTML")

    else:
        await call.message.answer(text='Hozircha Gilamlar mavjud emas!')


@dp.callback_query_handler(lambda callback: callback.data.split('_')[0] in ['back', 'work', 'next'])
async def callback_handler(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    id = callback.data.split('_')[2]
    sub_data = await db.get_products_sub(int(id))
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
    if stories[n - 1][-1] == True:
        await callback.message.answer_photo(photo=open(f"{BASE}/admin/media/{stories[n - 1][1]}", 'rb'),
                                            caption=f"<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {stories[n - 1][2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {stories[n - 1][3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {stories[n - 1][4]} x {stories[n - 1][5]}\n<b>Нархи:</b> {stories[n - 1][4] * stories[n - 1][5] * sub_data[-2]} сум\n\nНасия Савдо Мавжуд ✅"
                                            , reply_markup=btn, parse_mode="HTML")

    elif stories[n - 1][-1] == False:
        await callback.message.answer_photo(photo=open(f"{BASE}/admin/media/{stories[n - 1][1]}", 'rb'),
                                            caption=f"<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {stories[n - 1][2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {stories[n - 1][3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {stories[n - 1][4]} x {stories[n - 1][5]}\n<b>Нархи:</b> {stories[n - 1][4] * stories[n - 1][5] * sub_data[-2]} сум\n\nНасия Савдо Мавжуд Емас ❌"
                                            , reply_markup=btn, parse_mode="HTML")

    await callback.answer(str(f"📑 Siz shu sahifadasiz: {n}"))


@dp.message_handler(state=BoglanishState.phone, content_types=types.ContentType.CONTACT)
async def phone_handler(message: types.Message, state: FSMContext):
    try:
        await message.answer(
            "Телефон рақамингизни юборганингиз учун раҳмат!😊\n Тез орада операторларимиз сиз билан боғланишади 👩🏻‍💻",
            reply_markup=users_keyboard)
        async with state.proxy() as data:
            id = data['media_id']
            datas = await db.get_products(int(id))
            sub_data = await db.get_products_sub(int(id))

            for i in datas:
                await bot.send_message(chat_id=941535008,
                                       text=f"Mijoz Telefon raqami: {message.contact.phone_number}\n\nXarid qilmoqchi 🤝:\n\n<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {i[2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {i[3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {i[4]} x {i[5]}\n<b>Нархи:</b> {i[4] * i[5] * sub_data[-2]} сум\n")
        await state.finish()
    except Exception as e:
        print(f"An exception occurred: {e}")


@dp.message_handler(commands="start", state=BoglanishState.phone)
async def start_phone(message: types.Message, state: FSMContext):
    await message.answer("Bosh Menu 🏠", reply_markup=users_keyboard)
    await state.finish()
