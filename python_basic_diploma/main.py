from aiogram import executor
from loader import bot, dp, db
from handlers.default_hadlers import default_handlers
from handlers.custom_handlers import custom_handlers


async def on_startup(_):
    await db.db_start()
    print('БОТ ЗАПУЩЕН!')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)





