guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


while True:
    print('Сейчас на вечеринке,', len(guests), 'человек:', guests)
    move = input('Гость пришёл или ушёл? ')
    if move == 'пора спать':
        break
    name = input('Имя гостя: ')
    if move == 'пришёл' and len(guests) > 6 or len(guests) == 6:
        print('Прости,', name, 'но мест нет.')

    if move == 'пришёл' and len(guests) < 6:
        print('Привет,', name, '!')
        guests.append(name)
    if move == 'ушёл':
        print('Пока,', name, '.')
        guests.remove(name)

print('Вечеринка закончилась, все легли спать.')


