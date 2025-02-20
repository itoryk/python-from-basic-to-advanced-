import sys

import logging_tree

from utils import string_to_operator
import logging


logger = logging.getLogger('app')


def calc(args):
    logger.info(f"Arguments: {args}")

    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        logger.error("Error while converting number 1")
        logger.error(e)

    try:
        num_2 = float(num_2)
    except ValueError as e:
        logger.error("Error while converting number 1")
        logger.error(e)

    operator_func = string_to_operator(operator)

    result = operator_func(num_1, num_2)

    logger.debug(f'Result: {result}')
    logger.debug(f"{num_1} {operator} {num_2} = {result}")


if __name__ == '__main__':
    # calc(sys.argv[1:])
    calc('2+3')
    logging_tree.printout()
    with open('logging_tree.txt', 'w') as file:
        file.write(logging_tree.format.build_description())