from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='/description')
b3 = KeyboardButton(text='/city')
b4 = KeyboardButton(text='/listCity')
b5 = KeyboardButton(text='/history')

kb.add(b1, b2).add(b3, b4).add(b5)

