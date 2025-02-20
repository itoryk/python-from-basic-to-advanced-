def shift_string(first_string, second_string):
    step = 1
    test = False
    while step <= len(second_string):
        shift = first_string[-step:] + first_string[:-step]
        print(shift)
        if shift == second_string:
            test = True
            break
        step += 1
    return ''.join(['Первая строка получается из второй со сдвигом ', str(step)]) if test \
        else 'Первую строку нельзя получить из второй с помощью циклического сдвига.'


text_one = input('Первая строка: ')
text_two = input('Вторая строка: ')

print(shift_string(text_one, text_two))
