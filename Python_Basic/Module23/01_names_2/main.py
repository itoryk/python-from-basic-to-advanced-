total_chars = 0
line_number = 0
names = open('people.txt', 'r', encoding='utf-8')

for line in names:
    try:
        stripped_line = line.strip()
        line_number += 1
        if len(stripped_line) < 3:
            raise ValueError
        total_chars += len(stripped_line)

    except ValueError:
        print('Ошибка: Менее трёх символов в строке {}'.format(line_number))
        total_chars += len(stripped_line)

print('Общее количество символов:{}'.format(total_chars))

names.close()
