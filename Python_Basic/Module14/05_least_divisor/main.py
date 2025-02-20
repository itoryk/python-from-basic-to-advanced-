num = int(input('Введите число: '))
divider = 2

while (num % divider) != 0:
    divider = divider + 1

print('Наименьший делитель, отличный от единицы: ', divider)
