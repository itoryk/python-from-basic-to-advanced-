text = input('Введите строку: ').split()

word = [len(i) for i in text]

big_word = text[word.index(max(word))]

print('Самое длинное слово: ', big_word)
print('Длина этого слова: ', len(big_word))