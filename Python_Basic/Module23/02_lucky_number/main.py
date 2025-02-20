import random

count = 0

with open('out_file.txt', 'w') as numbers:
    while count < 777:
        number = int(input('Введите число: '))
        try:
            random_number = random.randint(1, 13)
            if number == random_number:
                raise('Вас постигла неудача!')
        finally:
            count += number
            numbers.write(str(number) + '\n')
    print('Вы успешно выполнили условие для выхода из порочного цикла!')

