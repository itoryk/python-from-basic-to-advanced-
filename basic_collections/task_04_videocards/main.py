def get_input_parameters():
    cards = int(input('Кол-во видеокарт: '))
    video_cards = []

    for i in range(1, cards + 1):
        print(i, 'Видеокарта: ', end='')
        card = int(input())
        video_cards.append(card)
    return video_cards


def display_result(old_video_cards, new_video_cards):
    print('Старый список видеокарт: ', old_video_cards)
    print('Новый список видеокарт: ', new_video_cards)
    pass


def select_video_cards(video_cards):
    m = max(video_cards)
    new_video_cards = video_cards.copy()
    for i in video_cards:
        if i == m:
            new_video_cards.remove(i)
    return new_video_cards


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    video_cards = get_input_parameters()  # получаем параметры
    result_video_cards = select_video_cards(video_cards)  # удаляет наибольшие элементы.
    display_result(video_cards, result_video_cards)  # выводим результат
