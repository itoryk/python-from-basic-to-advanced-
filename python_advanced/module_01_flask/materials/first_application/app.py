import datetime
from flask import Flask
from datetime import timedelta
import random
import os

app = Flask(__name__)

cars = "Chevrolet, Renault, Ford, Lada"
cats = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]
visits = 0


@app.route('/test')
def test_function():
    now = datetime.datetime.now().utcnow()
    return f'Это тестовая страничка, ответ сгенерирован в {now}'


@app.route('/hello')
def hello_world():
    return 'Привет, Мир!'


@app.route('/cars')
def car():
    return cars


@app.route('/cats')
def cat():
    return random.choice(cats)


@app.route('/get_time/now')
def current_time():
    now = datetime.datetime.now()
    time_now = now.strftime('%H:%M:%S')
    return f'Точное текущее время:{time_now}'


@app.route('/get_time/future')
def future():
    now = datetime.datetime.now()
    future_time = now + timedelta(hours=1)
    time = future_time.strftime('%H:%M:%S')
    return f'Точное время через час:{time}'


@app.route('/get_random_word')
def random_word():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    book_file = os.path.join(base_dir, '..\\..\\homework\\war_and_peace.txt')

    with open(book_file, 'rb') as book:
        word = book.readline().split()
    return random.choice(word)


@app.route('/counter')
def counter():
    global visits
    visits += 1
    count = str(visits)
    return count


