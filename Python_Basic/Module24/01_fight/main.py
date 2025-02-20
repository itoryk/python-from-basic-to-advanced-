import random


class Warrior:
    def __init__(self, name, health):
        self.name = name
        self.healthy = health

    def fight(self):
        bit = random.randint(1, 2)
        if bit == 1:
            self.healthy -= 20
        else:
            print('Мимо!')


warrior_1 = Warrior('Лёлик', 100)
warrior_2 = Warrior('Болик', 100)

while True:
    request = input(f'Кто атакует\n {warrior_1.name}/1 или {warrior_2.name}/2 ?')
    if request == '1':
        print(f'{warrior_1.name} атакует {warrior_2.name}')
        warrior_2.fight()
        print(f'У противника осталось здоровья - {warrior_2.healthy}')
    elif request == '2':
        print(f'{warrior_2.name} атакует {warrior_1.name}')
        warrior_1.fight()
        print(f'У противника осталось здоровья - {warrior_1.healthy}')

    if warrior_1.healthy <= 0:
        print(f'Игра окончена! Победил {warrior_2.name}')
        break
    elif warrior_2.healthy <= 0:
        print(f'Игра окончена! Победил {warrior_1.name}')
        break
