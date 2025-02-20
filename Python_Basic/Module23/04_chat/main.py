user_name = input('Как вас зовут? ')
while True:
    print('Чтобы увидеть текущий текст чата введите 1, чтобы написать сообщение введите 2')
    response = input('Введите 1 или 2\n')
    if response == '1':
        try:
            with open('chat.txt', 'r') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('Пока чат пуст')
    elif response == '2':
        new_messages = input('введите сообщение: \n')
        with open('chat.txt', 'a') as file:
            file.write('{name}: {messages}\n'.format(
                name=user_name, messages=new_messages
            ))

    else:
        print('ОШИБКА')