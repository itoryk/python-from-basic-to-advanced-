with open('zen.txt', 'r', encoding='UTF-8') as zen_file:
    for line in reversed(zen_file.readlines()):
        print(line, end='')

zen_file.close()

