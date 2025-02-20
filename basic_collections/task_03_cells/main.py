def get_input_parameters():
    num_of_cells = int(input('Кол-во клеток: '))
    cells = []
    for n in range(1, num_of_cells + 1):
        print('Эффективность',n,'клетки: ', end='')
        efficiency = int(input())
        cells.append(efficiency)
    return cells


def display_result(cells):
    print('Неподходящие значения: ', cells)
    pass


def select_cells(cells):
    new_cells = []
    for index in range(len(cells)):
        if index > cells[index]:
            new_cells. append(cells[index])
    return new_cells


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    cells = get_input_parameters()  # получаем параметры
    result_cells = select_cells(cells)  # отбираем клетки
    display_result(result_cells)  # выводим результат
