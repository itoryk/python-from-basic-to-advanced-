from typing import List
from functools import reduce

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]


third_power = lambda num: round(num ** 3, 3)
result1 = map(third_power, floats)
new_floats = list(result1)
print('Новый список floats: ', new_floats)

new_names = list(filter(lambda x: len(x) >= 5, names))
print('Новый список names: ', new_names)

new_numbers = reduce(lambda res, x: res*x, numbers, 1)
print('Произведение чисел в списке равно : ', new_numbers)
