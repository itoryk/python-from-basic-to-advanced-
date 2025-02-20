def search_items(list_1, list_2, list_3):
    similar_elements = []
    for element in list_1:
        if element in list_2 and element in list_3:
            similar_elements.append(element)
    return similar_elements


def difference_items(list_1, list_2, list_3):
    difference_elements = []
    for element in list_1:
        if element not in list_2 and element not in list_3:
            difference_elements.append(element)
    return difference_elements


def search_elements(list_1, list_2, list_3):
    similar_elements = set(list_1) & set(list_2) & set(list_3)
    return similar_elements


def search_difference(list_1, list_2, list_3):
    difference_element = set(list_1) - set(list_2) - set(list_3)
    return difference_element


array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]


print('\nЗадача 1:')
print('\n\tРешение без множеств: ', search_items(array_1, array_2, array_3))
print('\tРешение с множествами:', search_elements(array_1, array_2, array_3))
print('\nЗадача 2:')
print('\n\tРешение без множеств: ', difference_items(array_1, array_2, array_3))
print('\tРешение с множествами:', search_difference(array_1, array_2, array_3))


