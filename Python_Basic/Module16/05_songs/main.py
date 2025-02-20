violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

name = 0
total_time = 0

songs = int(input('Сколько песен выбрать? '))

for _ in range(songs):
    songs_name = input('Названиe песни: ')
    for song in violator_songs:
        if song[0] == songs_name:
            name += song.count(songs_name)
            time = song[1]
            total_time += time

print('Общее время звучания песен:', round(total_time, 2), 'минуты.')