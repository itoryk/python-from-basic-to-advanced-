class Student:
    def __init__(self, full_name, group_number, progress):
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress
        self.average = sum(progress) / len(progress)

    def give_average(self):
        return self.average

    def __str__(self):
        return f'{self.full_name} {self.group_number}'


def receiving_data():
    name = input('ФИ: ')
    group = input('Номер группы: ')
    progress = list(map(int, input('Оценки: ').split()))
    return name, group, progress


list_student = [Student(*receiving_data()) for _ in range(10)]
print('=====Список студентов=====')
for student in list_student:
    print(student)


list_student.sort(key=lambda x: x.give_average())
print('=====Список студентов отсортированный=====')
for student in list_student:
    print(student)




