import random


class House:
    def __init__(self):
        self.food = 50
        self.money = 0


class Person:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def to_eat(self):
        self.house.food -= 10
        self.satiety += 10
        print(f'{self.name} поел.\n'
              f'Сытость = {self.satiety}\n'
              f'В доме осталось {self.house.food} еды')

    def is_alive(self):
        return self.satiety > 0

    def to_work(self):
        self.satiety -= 10
        self.house.money += 10
        print(f'{self.name} поработал.\n'
              f'Сытость = {self.satiety}\n'
              f'В доме  {self.house.money} денег')

    def to_play(self):
        self.satiety -= 10
        print(f'{self.name} поиграл.\n'
              f'Сытость = {self.satiety}')

    def go_shop(self):
        self.house.food += 10
        self.house.money -= 10
        print(f'{self.name} сходил в магазин.\n'
              f'Продуктов в доме = {self.house.food}\n'
              f'В доме  {self.house.money} денег')


def one_day(person):
    cubes_number = random.randint(1, 6)
    if person.satiety < 0:
        print(f'К сожалению, {person.name} умер ')
        return 1
    if person.satiety < 20:
        person.to_eat()
    elif person.house.food < 10:
        person.go_shop()
    elif person.house.money < 50:
        person.to_work()
    elif cubes_number == 1:
        person.to_work()
    elif cubes_number == 2:
        person.to_eat()
    else:
        person.to_play()


def life():
   apartment = House()
   residents = [Person('Лёлик', apartment), Person('Болик', apartment)]
   day = 0
   while len(residents) > 0 and day < 366:
       day += 1
       for person in residents:
           one_day(person)
           if not person.is_alive():
               print(f'К сожалению, ваш {person.name} персонаж не пережил {day} день')
               residents.remove(person)

   print(f'Персонажи прожили {day} дней')


life()
