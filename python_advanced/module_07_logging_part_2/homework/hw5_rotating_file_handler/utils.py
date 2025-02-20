import logging.config
from config import dict_config
from typing import Union, Callable
from operator import sub, mul, truediv, add

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}

Numeric = Union[int, float]
logging.config.dictConfig(dict_config)
logger = logging.getLogger('my_logger.utils')


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    logger.info(f"String conversion '{value}' to arithmetic operator")

    if not isinstance(value, str):
        logger.error(f"wrong operator type {value}")
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        logger.error(f"wrong operator value {value}")
        raise ValueError("wrong operator value")

    return OPERATORS[value]
