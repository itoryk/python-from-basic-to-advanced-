letters = 'аяуюоеёэиы'
text = input('Введите текст: ')

count_vowel = [vowel for vowel in text if vowel in letters]

print('Список гласных букв: ',count_vowel,'\nДлина списка: ', len(count_vowel))