number_of_people = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке? '))

print('Значит, выбывает каждый', number, '-й человек')

people = list(range(1, number_of_people + 1))
start = 0

while len(people) > 1:
    print('\nТекущий круг людей:', people)
    start_count = start % len(people)
    print('Начало счёта с номера ', people[start_count])
    start = (start_count + number - 1) % len(people)
    print('Выбывает человек под номером', people[start])
    people.remove(people[start])
    print()
    print('Остался человек под номером', people)
