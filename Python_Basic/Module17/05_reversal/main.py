word = input('Введите строку: ')

reverse = word[word.find('h') + 1: word.rfind('h')]
word = reverse[::-1]

print('Развёрнутая последовательность между первым и последним h: ', word)