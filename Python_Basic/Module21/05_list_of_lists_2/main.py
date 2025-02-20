nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def unpacking(my_list):
    if not my_list:
        return []
    return unpacking(my_list[:-1]) + ([my_list[-1]] if not isinstance(my_list[-1], list) else unpacking(my_list[-1]))


print(unpacking(nice_list))