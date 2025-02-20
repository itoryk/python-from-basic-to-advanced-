from aiogram import Bot, Dispatcher, types
from config_data.config import TOKEN, API
#import json
#import requests
from database import db
#from handlers.default_hadlers import default_handlers


bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)