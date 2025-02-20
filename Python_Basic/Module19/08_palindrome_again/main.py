def palindrome(string):
    letters = {}
    for item in string:
        letters[item] = letters.get(item, 0) + 1
    count = 0
    for item in letters.values():
        if item % 2 != 0:
            count += 1

    return count <= 1


word = input('Введите строку:')

if palindrome(word):
    print('Можно сделать палиндромом')

else:
    print('Нельзя сделать палиндромом')