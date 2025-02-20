numbers = int(input('Введите количество пар слов: '))

synonyms = {}

for word in range(1, numbers+1):
    words = input('{0}-ая пара: '.format(word)).lower()
    words = words.split(' ')
    synonyms[words[0]] = words[2]

while True:
    test_word = input('Введите словo: ')
    if test_word in synonyms.keys():
        print('Синоним: ', synonyms[test_word])
        break
    if test_word in synonyms.values():
        inversion = {k: i for i, k in synonyms.items()}
        print('Синоним: ', inversion[test_word])
        break
    else:
        print('Такого слова в словаре нет.')