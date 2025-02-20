# from sympy import *


# def crypto(collections):
#     return[index for index, nums in enumerate(collections) if isprime(index)]

# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def crypto(collect):
    return[nums for index, nums in enumerate(collect) if is_prime(index)]


def is_prime(num):
    count = 0
    if num > 1:
        for i in range(2, num//2 + 1):
            if num % i == 0:
                count += 1
        if count == 0:
            return True
        else:
            return False


# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(crypto('О Дивный Новый мир!'))