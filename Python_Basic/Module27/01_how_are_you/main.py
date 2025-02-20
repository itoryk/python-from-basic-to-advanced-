from typing import Callable, Any
import functools


def nasty_func(func: Callable) -> Any:

    """"функция, которая спрашивает как дела"""

    @functools.wraps(func)
    def wrapp(*args, **kwargs):
        print('Как дела?')
        answer = input()
        print('А у меня не очень:(\nЛадно, держи свою функцию.')
        result = func(*args, **kwargs)
        return result
    return wrapp


@nasty_func
def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])

    return result


@nasty_func
def information(first_name: str, last_name: str):
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name


@nasty_func
def hard_func():
    return [x**2**x for x in range(5)]


print(squares_sum())
print(information('вася', 'пупкин'))
print(hard_func())

print(nasty_func.__name__)
print(nasty_func.__doc__)