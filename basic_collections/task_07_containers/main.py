def get_input_parameters():
    amount_of_containers = int(input('Кол-во контейнеров: '))
    containers = []
    for _ in range(amount_of_containers):
        weigh = int(input('Введите вес контейнера: '))
        containers.append(weigh)
        if weigh > 200:
            print('Ошибка! Контейнер не может весить больше, чем 200 кг')
            break
    new_container = int(input('Введите вес нового контейнера: '))
    if new_container > 200:
        print('Ошибка! Контейнер не может весить больше, чем 200 кг')
    return containers, new_container


def display_result(serial_number_new_container):
    print('Номер, куда встанет новый контейнер:', serial_number_new_container)


def search_serial_number_new_container(list_container_weights, new_container_weight):
    serial_number = 0
    while serial_number < len(list_container_weights) and list_container_weights[serial_number] >= new_container_weight:
        serial_number += 1
    return serial_number + 1


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    input_data = get_input_parameters()  # получаем параметры
    list_container_weights = input_data[0]
    new_container_weight = input_data[1]
    # Ищем куда вставим новый контейнер.
    serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)
    display_result(serial_number_new_container)  # выводим результат
