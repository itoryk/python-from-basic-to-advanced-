nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [num for l1 in nice_list for l2 in l1 for num in l2]
print(new_list)