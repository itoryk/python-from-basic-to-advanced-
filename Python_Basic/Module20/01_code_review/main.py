def student_description(dictionary):
    hobby = []
    surnames = ''
    for item in dictionary:
        hobby += (dictionary[item]['interests'])
        surnames += dictionary[item]['surname']
    count = 0
    for _ in surnames:
        count += 1
    return hobby, count


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


pairs = []
for i_id in students:
    pairs.append(students[i_id]['age'])
print('Список пар "ID студента — возраст": ', list(enumerate(pairs, start=1)))


hobbies = student_description(students)[0]
surname = student_description(students)[1]
print('Полный список интересов всех студентов: ', hobbies, '\nОбщая длина всех фамилий студентов: ', surname)




