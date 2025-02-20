def display_result(participants_names):
    print('Первый день: ', participants_names)



def get_participants_names(names):
    names = sorted(names[0:8:2])
    return names


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_participants_names и display_result
    participants_names = get_participants_names(
        ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    )  # получаем список имён с чётными индексами
    display_result(participants_names)  # выводим результат
