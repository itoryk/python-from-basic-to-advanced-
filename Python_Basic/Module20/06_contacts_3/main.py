def add_contact():
    request = input('Введите имя и фамилию нового контакта (через пробел):').lower()
    name = tuple(request.split())
    if name in phone_book:
        print('Такой человек уже есть в контактах.')
    else:
        phone_number = input('Введите номер телефона:')
        phone_book[name] = phone_number
        print('Текущий словарь контактов:', phone_book)


def search_contact():
    search = input('Введите фамилию для поиска:').lower()
    for name, number in phone_book.items():
        if search == name[1]:
            print(name[0], name[1], number)
        else:
            print('Такого контакта нет.')



phone_book = {}
while True:
    request = int(input('Введите номер действия:\n1. Добавить контакт\n2. Найти человека\n'))
    if request == 1:
        add_contact()
    if request == 2:
        search_contact()