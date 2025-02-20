def check_number(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def tpl_sort(my_tuple):
    flag = False
    for number in my_tuple:
        if check_number(str(number)) == flag:
            return my_tuple
    return tuple(sorted(my_tuple))


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))