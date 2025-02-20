"""
Ваш коллега, применив JsonAdapter из предыдущей задачи, сохранил логи работы его сайта за сутки
в файле skillbox_json_messages.log. Помогите ему собрать следующие данные:

1. Сколько было сообщений каждого уровня за сутки.
2. В какой час было больше всего логов.
3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
4. Сколько сообщений содержит слово dog.
5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
"""
import json
import subprocess
from collections import defaultdict
from itertools import groupby
from typing import Dict


def task1() -> Dict[str, int]:
    """
    1. Сколько было сообщений каждого уровня за сутки.
    @return: словарь вида {уровень: количество}
    """

    count = {'DEBUG': 0, 'ERROR': 0, 'WARNING': 0, 'CRITICAL': 0, 'INFO':0}
    for k, l in count.items():
        cmd = f"""grep -c '"level": "{k}"' skillbox_json_messages.log"""
        count[k] = int(subprocess.run(cmd, shell=True, stdout=subprocess.PIPE).stdout.decode())
    return count


def task2() -> int:
    """
    2. В какой час было больше всего логов.
    @return: час
    """
    hours = []
    for log_line in log_data:
        hours.append(log_line['time'][:2])
    groups = []
    unique_keys = []
    for k, g in groupby(hours):
        groups.append(len(list(g)))
        unique_keys.append(k)
    max_value = max(groups)
    max_value_index = groups.index(max_value)
    return int(unique_keys[max_value_index])


def task3() -> int:
    """
    3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
    @return: количество логов
    """
    cmd = f"""grep -E '"level": "CRITICAL"' skillbox_json_messages.log |
            grep -E '"time": "(05:([0-1][0-9]|19):[0-5][0-9])"' | wc -l"""
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE).stdout.decode()
    return int(result)


def task4() -> int:
    """
    4. Сколько сообщений содержат слово dog.
    @return: количество сообщений
    """
    cmd = f"""grep -E '"message": .+dog' skillbox_json_messages.log | wc -l"""
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE).stdout.decode()
    return int(result)


def task5() -> str:
    """
    5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
    @return: слово
    """
    messages = []
    for log_level in log_data:
        if log_level['level'] == 'WARNING':
            messages.append(log_level['message'])
    temp = defaultdict(int)
    for msg in messages:
        for word in msg.split():
            temp[word] += 1
    result = max(temp, key=temp.get)
    return result


if __name__ == '__main__':
    log_data = []
    with open('skillbox_json_messages.log', 'r') as file:
        for line in file.readlines():
            log_data.append(json.loads(line.rstrip()))
    tasks = (task1, task2, task3, task4, task5)
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f'{i}. {task_answer}')
