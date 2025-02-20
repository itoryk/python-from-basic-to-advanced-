def qsort(my_list):
    if len(my_list) <= 1:
        return my_list
    separator = my_list[-1]
    left = []
    middle = []
    right = []
    for a in my_list:
        if a < separator:
            left.append(a)
        elif a == separator:
            middle.append(a)
        else:
            right.append(a)
    return qsort(left) + middle + qsort(right)


numbers = [1, 2, 3, 5, -9, 4, -7, 3, 0, 0, 11, 18]

print(qsort(numbers))
