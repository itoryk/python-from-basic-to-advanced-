first_class = list(range(160, 176, 2))
second_class = list(range(162, 180, 3))

first_class.extend(second_class)

print(sorted(first_class))