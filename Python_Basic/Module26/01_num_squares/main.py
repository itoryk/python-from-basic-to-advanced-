'''класс-итератор'''


class MyIter:
    def __init__(self, number: int) -> None:
        self.number = number
        self.i_number = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        self.i_number += 1
        if self.i_number < self.number:
            return self.i_number ** 2
        else:
            raise StopIteration


my_iterator = MyIter(5)

print('Класс-итератор')

for num_sqr in my_iterator:
    print(f'{my_iterator.i_number} ** 2 = {num_sqr}')

'''функция - генератор'''


def my_generator(number):
    for i_number in range(1, number):
        yield i_number ** 2


my_generator = my_generator(5)

count = 0

print('функция - генератор')

for i_elem in my_generator:
    count += 1
    print(f'{count} ** 2 = {i_elem}')

'''генераторное выражение'''

generator_expression = (number ** 2 for number in range(1, 5))

count = 0

print('генераторное выражение')

for number in generator_expression:
    count += 1
    print(f'{count} ** 2 = {number}')