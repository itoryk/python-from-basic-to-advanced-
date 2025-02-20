with open('registrations.txt', 'r', encoding='utf-8') as registr_file:
    for i_index,i_line in enumerate(registr_file):
        try:
            line_list = i_line.split()
            if len(line_list) < 3:
                raise IndexError
            else:
                for letters in line_list[0]:
                    if not letters.isalpha():
                        raise NameError
                if '@' and '.' not in line_list[1]:
                    raise SyntaxError
                if line_list[2].isdigit():
                    if not 10 < int(line_list[2]) < 99:
                        raise ValueError
                else:
                    raise ValueError
        except IndexError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as registr_bad_file:
                registr_bad_file.write(f'НОМЕР СТРОКИ: {i_index+1}\n{i_line}    '
                                       f'НЕ ПРИСУТСВУЮТ ВСЕ ТРИ ПОЛЯ\n')
        except NameError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as registr_bad_file:
                registr_bad_file.write(f'НОМЕР СТРОКИ: {i_index + 1}\n{i_line}    '
                                        f'ПОЛЕ ИМЯ СОДЕРЖИТ НЕ ТОЛЬКО БУКВЫ\n')
        except SyntaxError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as registr_bad_file:
                registr_bad_file.write(f'НОМЕР СТРОКИ: {i_index + 1}\n{i_line}    '
                                        f'ПОЛЕ ИМЕЙЛ НЕ СОДЕРЖИТ @ И .\n')
        except ValueError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as registr_bad_file:
                registr_bad_file.write(f'НОМЕР СТРОКИ: {i_index + 1}\n{i_line}    '
                                        f'ПОЛЕ ВОЗРАСТ НЕ ЯВДЯЕТСЯ ЧИСЛОМ ОТ 10 ДО 99\n')
        else:
            with open('registrations_good.log', 'a', encoding='utf-8') as registr_good_file:
                registr_good_file.write(f'{i_line}')



