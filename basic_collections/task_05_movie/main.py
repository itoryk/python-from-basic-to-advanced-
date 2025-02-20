def get_input_parameters():
    favorite_films = []
    num = int(input('Сколько фильмов хотите добавить? '))
    for i in range(num):
        film = input('Введите название фильма: ')
        favorite_films.append(film)
    return favorite_films


def display_result(favorite_films, errors):
    while len(errors) != 0:
        error = errors.pop()
        print('Ошибка: фильма ', error, 'у нас нет :(')
    print('Ваш список любимых фильмов: ', favorite_films)


def add_favorite_film(new_favorite_films, available_films):
    errors = []
    for film in new_favorite_films:
        if film in available_films:
            film = new_favorite_films
        else:
            new_favorite_films.remove(film)
            errors.append(film)

    return new_favorite_films, errors
if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    available_films = [
        "Крепкий орешек", "Назад в будущее", "Таксист",
        "Леон", "Богемская рапсодия", "Город грехов",
        "Мементо", "Отступники", "Деревня"
    ]
    new_favorite_films = get_input_parameters()  # получаем параметры
    favorite_films, errors = add_favorite_film(
        new_favorite_films,
        available_films
    )  # добавлем фильмы в список "любимых".
    display_result(favorite_films, errors)  # выводим результат
