"""
Реализуйте endpoint, начинающийся с /max_number, в который можно передать список чисел, разделённых слешем /.
Endpoint должен вернуть текст «Максимальное переданное число {number}»,
где number — выделенное курсивом наибольшее из переданных чисел.

Примеры:

/max_number/10/2/9/1
Максимальное число: 10

/max_number/1/1/1/1/1/1/1/2
Максимальное число: 2

"""

from flask import Flask

app = Flask(__name__)


@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    numbers = numbers.split('/')
    try:
        nums_int = [int(x) for x in numbers]
    except ValueError:
        return 'Error! should be only numbers.'

    return f'Maximum number of: {max(nums_int)}'


if __name__ == "__main__":
    app.run(debug=True)
