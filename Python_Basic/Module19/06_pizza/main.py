orders = int(input('Введите количество заказов: '))

global_info = {}

for number in range(1, orders+1):
    info = input('{0} заказ: '.format(number))
    info = info.split(' ')
    if info[0] in global_info:
        if info[1] in global_info[info[0]]:
            global_info[info[0]][info[1]] += int(info[2])
        else:
            global_info[info[0]][info[1]] = info[2]
    else:
        global_info[info[0]] = dict({info[1]: int(info[2])})


for item_1 in sorted(global_info):
    print(f'\n{item_1}:')
    for item_2 in sorted(global_info[item_1]):
        print(f'\t{item_2}: {global_info[item_1][item_2]}')