import re

numbers = ['9999999999', '999999-999', '99999x9999']


def check_numbers(numbers):
    names = ['первый номер:', 'второй номер:', 'третий номер:']
    count = -1
    for i in numbers:
        count += 1
        result = re.findall(r'[8-9]\d{9}', i)
        if len(result) == 1:
            print(names[count], 'всё в порядке')
        else:
            print(names[count], 'не подходит')


check_numbers(numbers)
