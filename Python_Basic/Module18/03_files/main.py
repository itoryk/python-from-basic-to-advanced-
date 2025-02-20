file = input('Название файла: ')
special_symbol = '@№$%^&\*()'

for symbol in special_symbol:
    if file.startswith(symbol):
        print('Ошибка: название начинается на один из специальных символов.')

if file.endswith('.txt') or file.endswith('.docx'):
    print('Файл назван верно.')
else:
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')