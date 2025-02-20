import os
from collections.abc import Iterable


def found_file_py(directory: str) -> Iterable[tuple]:
    for root, dirs, files in os.walk(directory):
        for file in files:
            count = 0
            if os.path.join(root, file).endswith('.py'):
                current_file = open(os.path.join(root, file), 'r', encoding='utf-8')
                for line in current_file.readlines():
                    if not (line == '\n' or line.strip().startswith(('"', '#', "'"))):
                        count += 1

            yield os.path.join(root, file), count


for i_elem in found_file_py(directory='..'):
    print(f'Файл {i_elem[0]}: строк кода - {i_elem[1]}')




