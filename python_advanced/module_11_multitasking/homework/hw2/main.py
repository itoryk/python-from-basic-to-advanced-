import logging
import sqlite3
import threading
import time
from typing import List
import requests


logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)

URL: str = 'https://swapi.dev/api/people/'

count = 1

def get_hero(url: str):
    global count
    response: requests.Response = requests.get(url, timeout=(30))
    if response.status_code != 200:
        return
    data = response.json()

    if data is not None:
        hero = (count, data['name'], data['birth_year'], data['gender'])
        cursor.execute(f'INSERT INTO heroes (id, name, age, gender) VALUES(?,?,?,?)', hero)
    count += 1

def load_heroes() -> None:
    start: float = time.time()
    for i in range(0,20):
        get_hero(URL + str(i))
    logger.info('Done in {:.4}'.format(time.time() - start))

def load_heroes_multithreading() -> None:
    start: float = time.time()
    threads: List[threading.Thread] = []
    for i in range(0,20):
        thread = threading.Thread(target=get_hero, args=(URL + str(i),))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    logger.info('Done in {:.4}'.format(time.time() - start))

if __name__ == '__main__':
    with sqlite3.connect('star_wars_heroes_db.sqlite3', check_same_thread=False) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS heroes (id INTEGER, name TEXT NOT NULL,
            age TEXT NOT NULL, gender TEXT NOT NULL)
        """)
        load_heroes()
        load_heroes_multithreading()