number = int(input('Введите длину списка: '))

numbers = [1 if num % 2 == 0 or num == 1 else num % 5 for num in range(number)]

print('Результат:', numbers)