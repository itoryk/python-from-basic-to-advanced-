"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(BASE_DIR, 'output_file.txt')


def get_summary_rss(ps_output_file_path: str) -> str:
    with open(ps_output_file_path, 'r') as file:
        lines = file.readlines()[1:]
    summ = 0
    for line in lines:
        columns = line.split()
        summ += int(columns[5])

    thousand = 1024
    label = 0

    labels = {0: 'kilo', 1: 'mega', 2: 'giga', 3: 'tera'}
    while summ > thousand:
        summ /= thousand
        label +=1
    return f'Amount of used memoty {round(summ, 3)} {labels[label]} bytes.'


if __name__ == '__main__':
    path: str = OUTPUT_FILE
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)
