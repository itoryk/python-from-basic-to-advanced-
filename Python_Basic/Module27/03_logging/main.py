import datetime
import math
from typing import Callable, Any


def logging(func: Callable) -> Any:

    file = open('function_errors.log', 'a')
    time = str(datetime.datetime.today())

    def wrap(*args, **kwargs):
        print(func.__name__, '\t ', func.__doc__)

        try:
            func(*args, **kwargs)

        except (TypeError, ZeroDivisionError):
            file.write(func.__name__ + '\t' + time + '\n')

        finally:
            logging(func)
            file.close()

    return wrap


@logging
def information(name, **kwargs):

    '''Функция, которая выводит на экран имя ученика и его оценки'''

    print(f'My name is {name}')
    for a, b in kwargs.items():
        print(f'{a}:{b}')


@logging
def display_info(name: str, age: int):
    '''Функция, которая выводит на экран имя и возраст'''
    print(name + ' ' + age)


@logging
def round_number(number: float):

    '''Функция, которая округляет число с плавающей точкой'''

    result = math.ceil(number)
    print(result)


@logging
def divisor(number: int):

    '''Функция, которая делит на ноль'''

    result = number // 0
    return result


information('Viktoria', math='3', history='5', english='4', biology='4')
display_info('Виктория', 27)
round_number(2.3)
divisor(5)
