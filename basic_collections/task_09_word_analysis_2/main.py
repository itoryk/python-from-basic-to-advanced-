def get_input_parameters():
    word = input('Введите слово: ')
    return word


def display_result(is_palindrome):
    if is_palindrome == True:
        print('Слово является палиндромом')
    else:
        print('Слово не является палиндромом')


def check_palindrome(word):
    is_palindrome = True
    word = list(word)
    for i in range(len(word)):
        if word[i] != word[-i - 1]:
            is_palindrome = False
    return is_palindrome


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    is_palindrome = check_palindrome(word)  # является ли слово палиндромом.
    display_result(is_palindrome)  # выводим результат
