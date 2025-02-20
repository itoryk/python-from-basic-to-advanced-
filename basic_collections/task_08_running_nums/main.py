def get_input_parameters():
    shift_number = int(input('Сдвиг: '))
    list_number = [1, 2, 3, 4, 5, 6, 7, 8]
    return  shift_number, list_number


def display_result(shifted_list):
    print('Сдвинутый список: ', shifted_list)


def shift_list(shift, original_list):
    original_list = original_list[-shift:] + original_list[:-shift]

    return original_list

if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    input_data = get_input_parameters()  # получаем параметры
    shift = input_data[0]
    original_list = input_data[1]
    shifted_list = shift_list(shift, original_list)  # сдвигаем список.
    display_result(shifted_list)  # выводим результат
