first_list = []
second_list = []

for num in range(1, 3+1):
    number = int(input(f'Введите {num}-oe число для первого списка: '))
    first_list.append(number)

for num in range(1, 7+1):
    number = int(input(f'Введите {num}-oe число для второго списка: '))
    second_list.append(number)


print('Первый список: ', first_list)
print('Второй список: ', second_list)

first_list.extend(second_list)

new_list = set(first_list)

print('Новый первый список с уникальными элементами: ', new_list)