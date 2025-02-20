import random


class Child:
    calm_status = {0: 'спокоен ', 1: 'плачет '}
    hungry_status = {0: 'сытый ', 1: 'голодный '}

    def __init__(self, child_name, child_age):
        self.name = child_name
        self.age = child_age
        self.calm_status = 0
        self.hungry_status = 0

    def child_info(self):
        print(f'Ребенку {self.name} {self.age} лет')

    def print_status(self):
        print('Ребенок {} сейчас {}'.format(self.name, Child.calm_status[self.calm_status]))
        print('Ребенок {} сейчас {}'.format(self.name, Child.hungry_status[self.hungry_status]))


class Parent:

    def __init__(self, parent_name, parent_age, child, child_count):
        self.name = parent_name
        self.age = parent_age
        self.child = []
        self.child_count = 0

    def parent_info(self):
        print(f'Меня зовут {self.name}, мне {self.age} лет, у меня {self.child_count} детей:')
        for i_child in self.child:
            i_child.child_info()
        print()

    def calm_the_child(self, child):
        if child.calm_status == 1:
            print(f' {self.name} успокаивает {child.name}! ')
            child.calm_status = 0
        else:
            print(f'{child.name} спокойный! ')

    def feed_the_child(self, child):
        if child.calm_status == 1:
            print(f' {self.name} кормит {child.name}! ')
            child.calm_status = 0
        else:
            print(f' {child.name} сытый! ')

    def add_child(self):
        count = int(input('Cколько детей?'))
        for i in range(count):

            child_1Name = input('Как зовут ребенка? ')
            child_1Age = int(input(f'Сколько {child_1Name} лет? '))
            if parentAge - child_1Age < 16:
                raise Exception("It's impossable")
            child_1 = Child(child_1Name, child_1Age)
            parent.child.append(child_1)
            parent.child_count = count



parentName = input('Как зовут родителя? ')
parentAge = int(input(f'Сколько {parentName} лет? '))
parent = Parent(parentName, parentAge, child=[], child_count=0)



parent.add_child()
parent.parent_info()


for i_child in parent.child:
    i_child.calm_state = random.randint(0, 1)
    i_child.hungry_state = random.randint(0, 1)
    i_child.print_status()
    parent.calm_the_child(i_child)
    parent.feed_the_child(i_child)
