import os

from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены')
else:
    load_dotenv()

TOKEN = os.getenv("TOKEN")
API = os.getenv("API")

