friends = int(input('Кол-во друзей: '))
promissory_notes = int(input('Кол-во долговых расписок: '))
friends_list = []

for _ in range(friends):
    friends_list.append(0)

for number in range(promissory_notes):
    print(number + 1, '-я расписка: ')
    to_who = int(input('Кому: '))
    from_who = int(input('От кого: '))
    how_much = int(input('Сколько: '))
    friends_list[from_who - 1] += how_much
    friends_list[to_who - 1] -= how_much

print('Баланс друзей: ')

for index in range(len(friends_list)):
    print(index + 1, ': ', friends_list[index])
