from loader import types
from loader import dp
from keyboard.reply.reply_keyboards import kb

HELP_COMMAND = '''
<b>/help</b> - <em>список команд</em> 
<b>/start</b> - <em>запуск бота</em> 
<b>/description</b> - <em>описание бота</em>
<b>/city</b> - <em>ввести город самостоятельно</em>
<b>/listCity</b> - <em>выбрать город из уже существующего списка</em>
<b>/history</b> - <em>история запросов</em>
'''


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text='Добро пожаловать!👋🏻', reply_markup=kb)

    await message.delete()


@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode='HTML')

    await message.delete()


@dp.message_handler(commands=['description'])
async def cmd_help(message: types.Message):
    await message.answer(text='Этот бот выводит погоду, влажность и координаты.')

    await message.delete()