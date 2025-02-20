def get_input_parameters():
    words = input('Введите слово: ')
    return words


def display_result(number_unique_letters):
    print('Кол-во уникальных букв: ', number_unique_letters)


def count_number_unique_letters(word):
    dictionary = []
    for letter in range(len(word)):
        if word.count(word[letter]) == 1:
            dictionary.append(word[letter])
    dictionary = len(dictionary)
    return dictionary


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    number_unique_letters = count_number_unique_letters(word)  # считаем количество уникальных букв.
    display_result(number_unique_letters)  # выводим результат
