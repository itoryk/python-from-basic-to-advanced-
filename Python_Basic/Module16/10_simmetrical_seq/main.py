def is_palindrome(num_list):
    reverse_list = []
    for i_num in range(len(num_list) -1, -1, -1):
        reverse_list.append(num_list[i_num])
    if num_list == reverse_list:
        return True
    else:
        return False


nums = int(input('Кол-во чисел: '))
numbers = []
for _ in range(nums):
    num = int(input('Число: '))
    numbers.append(num)

new_nums = []
answer = []

for i_nums in range(0, len(numbers)):
    for j_elem in range(i_nums,len(numbers)):
        new_nums.append(numbers[j_elem])
    if is_palindrome(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(numbers[i_answer])
        answer.reverse()
        break
    new_nums = []

print('Последовательность: ', numbers)
print('Нужно приписать чисел: ', len(answer))
print('Сами числа:', answer)