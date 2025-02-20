summ = 0
with open('numbers.txt', 'r') as my_file, open('answer.txt', 'w') as new_file:
    for line in my_file.read().split():
        summ += int(line)
    summ = str(summ)
    new_file.write(summ)


my_file.close()
new_file.close()