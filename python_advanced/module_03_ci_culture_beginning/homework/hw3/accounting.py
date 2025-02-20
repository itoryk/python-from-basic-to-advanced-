import datetime
from flask import Flask


app = Flask(__name__)

storage = {}


@app.route("/check")
def test():
    return "this is work!"


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:8])
    if check_date(year, month, day):
        storage.setdefault(year, {}).setdefault(month, {}).setdefault(day, 0)
        storage[year][month][day] += number
        return f'data is saved'
    else:
        return 'information is incorrect'


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    summ = 0
    data = storage[year]
    try:
        for expense in data.values():
            for i in expense.values():
                summ += i
        return {'result': summ}
    except KeyError:
        return f'not yet available data for {year} year.'


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    data = storage[year][month]
    summ = 0
    try:
        for i in data.values():
            summ += i
        return {'result': summ}
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




