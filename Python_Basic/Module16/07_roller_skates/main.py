skates = int(input('Кол-во коньков: '))
skates_size = []
for num in range(1, skates+1):
    size = int(input(f'Размер {num}-й пары:'))
    skates_size.append(size)

people = int(input('Кол-во людей: '))
people_size = []
for num in range(1, people+1):
    size = int(input(f'Размер ноги {num}-го человека:'))
    people_size.append(size)

available_skates = 0
for num in people_size:
    for i in range(len(skates_size)):
        if skates_size[i] >= num:
            skates_size.remove(skates_size[i])
            available_skates += 1
            break

print('Наибольшее кол-во людей, которые могут взять ролики: ', available_skates)