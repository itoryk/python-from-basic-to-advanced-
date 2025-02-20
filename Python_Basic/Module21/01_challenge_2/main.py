def print_numbers(num):
    if num != 0:
        print_numbers(num-1)
        print(num)


number = int(input('Введите num: '))

print_numbers(number)