def caesar_cipher(string, user_shift):
    char_list = [(alfabet[(alfabet.index(sym) + user_shift) % 33] if sym != ' ' else ' ')for sym in string]
    new_str = []
    for i_char in char_list:
        new_str += i_char
    return new_str


alfabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

out_str = caesar_cipher(message, shift)

print(out_str)