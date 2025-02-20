from typing import Iterable


def summ(*args):
    return sum(summ(*arg) if isinstance(arg, Iterable) else arg for arg in args)


print(summ([[1, 2, [3]], [1], 3]))
print(summ(1, 2, 3, 4, 5))
