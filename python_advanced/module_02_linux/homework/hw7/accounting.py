"""
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
"""
import datetime
from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:8])
    if check_date(year,month, day):
        storage.setdefault(year, {}).setdefault(month, 0)
        storage[year][month] += number
        return f'data is saved'
    else:
        return 'information is incorrect'


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    summ = 0
    try:
        for expense in storage[year].values():
            summ += expense
        return f'expenses for the {year} year were {summ} RUB.'
    except KeyError:
        return f'not yet available data for {year} year.'


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    try:
        return f'expenses for the {year} year and {month} month were {storage [year] [month]}.'
    except KeyError:
        return f'not yet available data for {year} year and {month} month.'


def check_date(year, month, day):
    try:
        datetime.datetime(year, month, day)
        correct_date = True
    except ValueError:
        correct_date = False
    return correct_date


if __name__ == "__main__":
    app.run(debug=True)
