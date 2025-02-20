from typing import Callable, Any
import time
import functools


def timer(func: Callable) -> Any:
    """функция, которая замедляет отработку обёртываемой функции"""
    @functools.wraps(func)
    def wrapp(*args, **kwargs):
        print('Твоя функция отработает через 5 секунд.')
        time.sleep(5)
        result = func(*args, **kwargs)
        return result
    return wrapp


def get_some_salad(func):
    def wrap(*args, **kwargs):
        print('#помидор#')
        func(*args, **kwargs)
        print('~салат~')
    return wrap


def get_some_bans(func):
    def wrap(*args, **kwargs):
        print("</------\>")
        func(*args, **kwargs)
        print("<\______/>")
    return wrap


@timer
@get_some_bans
@get_some_salad
def filler_burger(filler):
    print(filler)


filler_burger('ветчина')
print(timer.__name__)
print(timer.__doc__)