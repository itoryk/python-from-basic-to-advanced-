"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys


def get_mean_size(ls_output: str) -> float:
    summ = 0
    count = 0
    for line in ls_output:
        count += 1
        summ += int(line.split()[4])
    return summ / count


if __name__ == '__main__':
    data: list = sys.stdin.readlines()[1:]
    if not data:
        print('This directory is empty and cannot be accessed')
    else:
        mean_size: float = get_mean_size(data)
        print(mean_size)
