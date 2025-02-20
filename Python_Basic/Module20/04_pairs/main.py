import random

my_list = []
for _ in range(10):
    number = random.randint(0, 100)
    my_list.append(number)

print('Оригинальный список:', my_list)

origin_list = [number for number in (zip(my_list[::2], my_list[1::2]))]

print('Новый список:', origin_list)