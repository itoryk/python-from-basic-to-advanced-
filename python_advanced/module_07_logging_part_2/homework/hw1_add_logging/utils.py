import logging
from typing import Union, Callable
from operator import sub, mul, truediv, add


OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}

Numeric = Union[int, float]
logger = logging.getLogger('utils')
logger.setLevel('ERROR')
formatter = logging.Formatter('%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    if not isinstance(value, str):
        #print("wrong operator type", value)
        logger.error(f'wrong operator type {value}')
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        #print("wrong operator value", value)
        logger.error(f'wrong operator value {value}')
        raise ValueError("wrong operator value")

    return OPERATORS[value]
