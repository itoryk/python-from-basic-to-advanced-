def get_input_parameters():
    list_number = [1, 4, -3, 0, 10]
    return list_number


def display_result(sorted_list):
    print(sorted_list)


def sort_list(original_list):
    original_list.sort()
    return original_list


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    original_list = get_input_parameters()  # получаем параметры
    sorted_list = sort_list(original_list)  # сортируем список.
    display_result(sorted_list)  # выводим результат
