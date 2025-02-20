import logging
import multiprocessing
import sqlite3
import time
from os import cpu_count

import requests
from multiprocessing.pool import ThreadPool

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)

URL: str = 'https://swapi.dev/api/people/'

def links():
    link = []
    for i in range(0,20):
        link.append(URL + str(i))
    return link

def get_hero(url: str):
    response: requests.Response = requests.get(url, timeout=(30))
    if response.status_code != 200:
        return
    data = response.json()
    hero = (data['name'], data['birth_year'], data['gender'])
    print(hero)
    return hero

def load_heroes() -> None:
    start: float = time.time()
    for i in range(0,20):
        get_hero(URL + str(i))
    logger.info('Done in {:.4}'.format(time.time() - start))


def heroes_pool():
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    start: float = time.time()
    result = pool.map(get_hero, links())
    pool.close()
    pool.join()
    end: float = time.time()
    logger.info(f'runtime pool - {end - start}')
    return result

def heroes_threadpool():
    pool = ThreadPool(processes=multiprocessing.cpu_count())
    start: float = time.time()
    result = pool.map(get_hero, links())
    pool.close()
    pool.join()
    end: float = time.time()
    logger.info(f'runtime Threadpool - {end - start}')
    return result

def save_heroes(heroes):
    with sqlite3.connect('star_wars_heroes_db.sqlite3', check_same_thread=False) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS heroes (id INTEGER, name TEXT NOT NULL,
            age TEXT NOT NULL, gender TEXT NOT NULL)
        """)
        for hero in heroes:
            cursor.execute(f'INSERT INTO heroes (id, name, age, gender) VALUES(?,?,?,?)', hero)



if __name__ == '__main__':
    #load_heroes()
    #heroes_pool = heroes_pool()
    #save_heroes(heroes_pool)
    heroes_threadpool = heroes_threadpool()
    save_heroes(heroes_threadpool)