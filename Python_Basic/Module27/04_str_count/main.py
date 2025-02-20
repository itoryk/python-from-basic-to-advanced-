from typing import Callable
import functools


def counter(func: Callable) -> Callable:
    '''функция, которая считает кол-во вызовов'''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__, func.__doc__)
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@counter
def func():
    '''вызываемая функция'''

    print('Функция - 1')


func()
func()
func()

print(func.count)
print(counter.__name__, counter.__doc__)