import sys
from utils import string_to_operator
from logger_helper import get_logger

logger = get_logger('app')


def calc(args):
    #print("Arguments: ", args)
    logger.debug(f'Arguments: {args}')
    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        logger.error(f'Error while converting number 1')
        logger.error(e)
        #print("Error while converting number 1")
        #print(e)

    try:
        num_2 = float(num_2)
    except ValueError as e:
        logger.error(f'Error while converting number 1')
        logger.error(e)
        #print("Error while converting number 1")
        #print(e)

    operator_func = string_to_operator(operator)

    result = operator_func(num_1, num_2)

    logger.debug(f'result: {result}')
    logger.debug(f"{num_1} {operator} {num_2} = {result}")
    #print("Result: ", result)
    #print(f"{num_1} {operator} {num_2} = {result}")


if __name__ == '__main__':
    # calc(sys.argv[1:])
    calc('2+i')
