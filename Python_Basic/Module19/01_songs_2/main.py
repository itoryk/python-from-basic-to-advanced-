violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

number_of_songs = int(input('Сколько песен выбрать? '))
all_time = 0
for song in range(number_of_songs):
    name_song = input('Название {0} песни: '.format(song + 1))
    time_song = list()
    if name_song in violator_songs:
        time_song.append(violator_songs.get(name_song))
    for time in time_song:
        all_time += time

print('Общее время звучания песен: {0} минуты'.format(round(all_time, 2)))