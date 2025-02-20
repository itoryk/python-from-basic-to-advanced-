from loader import dp,types,db, API

import requests
import json


@dp.message_handler(commands=['history'])
async def history(message: types.Message):
    list_name = await db.get_list(message.from_user.id)
    result_string = ''
    for item in list_name:
        for i in item:
            result_string += i + '\n'
    await message.answer('История ваших запросов.')
    await message.reply(result_string.strip())


@dp.message_handler(commands=['listCity'])
async def list_city(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.InlineKeyboardButton('Минск'))
    markup.add(types.InlineKeyboardButton('Витебск'))
    markup.add(types.InlineKeyboardButton('Гродно'))
    markup.add(types.InlineKeyboardButton('Брест'))
    markup.add(types.InlineKeyboardButton('Могилёв'))
    markup.add(types.InlineKeyboardButton('Гомель'))
    await message.answer(text='Введите город', reply_markup=markup)
    await message.reply('Выберите город из списка')

# reply_markup=markup

@dp.message_handler(commands=['city'])
async def city(message: types.Message):
    await message.answer(text='Введите город')

    await message.delete()


@dp.message_handler(content_types=['text'])
async def reply(message: types.Message):
    city = message.text.lower().strip()
    await db.add_info(message.from_user.id, city)
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&appid={API}&units=metric'
    res = requests.get(url)
    data = json.loads(res.text)
    if res.status_code==200:
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        hum = data["main"]["humidity"]
        coord_lon = data["coord"]["lon"]
        coord_lat = data["coord"]["lat"]
        max = data["main"]["temp_max"]
        min = data["main"]["temp_min"]
        des = data["weather"][0]["description"]
        icon = data['weather'][0]['icon']
        file = open(f'./utils/img/{icon}@2x.png', 'rb')

        await message.reply(f'Погода в городе {message.text}\n'
                            f'Температура {temp} ℃\n'
                            f'Ощущается как {feels_like} ℃\n'
                            f'Влажность воздуха {hum} %\n'
                            f'Координаты. Широта: {coord_lon}\n'
                            f'Координаты. Долгота: {coord_lat}\n'
                            f'Максимальная температура воздуха {max} ℃\n'
                            f'Минимальная температура воздуха {min} ℃\n'
                            f'Описание: {des}')
        await message.answer_photo(file)

    elif res.status_code==404:
        await message.reply('Город не найден.')