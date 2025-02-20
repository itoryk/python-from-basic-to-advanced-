from random import uniform

first_team = [round(uniform(5, 10), 2) for i in range(20)]
second_team = [round(uniform(5, 10), 2) for i in range(20)]
winners = [ first_team[i] if first_team[i] > second_team[i] else second_team[i] for i in range(20)]

print('Первая команда: ', first_team, '\nВторая команда: ', second_team, '\nПобедители тура: ', winners)