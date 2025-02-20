list1 = [1, 5, 3]
list2 = [1, 5, 1, 5]
list3 = [1, 3, 1, 5, 3, 3]

list1.extend(list2)
print('Кол-во цифр 5 при первом объединении:', list1.count(5))

if 5 in list1:
    list1.remove(5)

list1.extend(list3)
print('Кол-во цифр 3 при первом объединении:', list1.count(3))
print('Итоговый список:', list1)

