import datetime

with open('logger.txt', 'r') as file:
    log_data = file.readlines()

odd_data = []
even_data = []

for k in range(30):
    if k % 2 != 0:
        odd_data.append(log_data[k].rstrip())
    else:
        even_data.append(log_data[k].rstrip())

zipped_data = list(zip(odd_data, even_data))

data_list = []

for v in zipped_data:
    obj_time = datetime.datetime.strptime(v[0][:9], '%M:%S.%f')
    obj_time2 = datetime.datetime.strptime(v[1][:9], '%M:%S.%f')
    result = obj_time - obj_time2
    data_list.append(result.microseconds / 1000)
average_time = sum(data_list) / 15

print(f'Average turnaround time: {round(average_time, 2)} microseconds')