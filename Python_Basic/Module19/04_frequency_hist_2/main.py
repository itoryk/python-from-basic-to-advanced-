import collections
def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1

    return sym_dict


text = input('Введите текст: ').lower()

print('Оригинальный словарь частот: ')

letters = {}

for sym in histogram(text):
    print(sym, ':', histogram(text)[sym])

for letter, number in collections.Counter(text).items():
    letters.setdefault(number, []).append(letter)

print('Инвертированный словарь частот: ')

for i_symb in letters:
    print(i_symb, ':', letters[i_symb])

