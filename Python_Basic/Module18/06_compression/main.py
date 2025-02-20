text = input('Введите строку: ')

new_text = ''

count = 1

for symbol in range(len(text) - 1):
    if text[symbol] == text[symbol + 1]:
        count += 1
    if text[symbol] != text[symbol + 1] or symbol == len(text) - 2:
        new_text += text[symbol] + str(count)
        count = 1
if text[-2] != text[-1]:
    new_text += text[-1] + '1'

print('Закодированная строка:', new_text)