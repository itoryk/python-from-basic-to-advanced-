while True:
    password = input('Придумайте пароль: ')
    if (sum(letter.isupper() for letter in password) < 1) \
            or (sum(letter.isnumeric() for letter in password) < 3) \
            or (len(password) < 8):
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break

