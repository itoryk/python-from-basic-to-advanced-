def reverse_float(num):
    parts = str(num).split('.')
    reversed_parts = [''.join(reversed(part)) for part in parts]

    return float('.'.join(reversed_parts))

n = reverse_float(input('Введите первое число: '))
k = reverse_float(input('Введите второе число: '))

print('Первое число наоборот: ', n)
print('Второе число наоборот: ', k)
print('Сумма: ', n + k)

