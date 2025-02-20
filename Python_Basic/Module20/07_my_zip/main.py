def length(string,tpl):
    return min(len(string), len(tpl))


my_string = 'abcd'
my_tuple = (10, 20, 30, 40)

pairs = ((my_string[elem], my_tuple[elem]) for elem in range(length(my_string,my_tuple)))

print(pairs)
for elem in pairs:
    print(elem)