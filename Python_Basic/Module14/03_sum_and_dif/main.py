summa = int(input('Введите число:'))
def sum_of_digits(summa):
    num = 0
    while summa > 0:
        num += summa % 10
        summa //= 10
    return num
def count_of_digits(summa):
    count = 0
    while(summa > 0):
        count = count + 1
        summa = summa // 10
    return count


num = sum_of_digits(summa)
count = count_of_digits(summa)

print('Сумма цифр равна: ', num)
print('Количество цифр равно: ', count)
print('Разность: ', num - count)



