import sqlite3

if __name__ == '__main__':
    response = []
    with sqlite3.connect('../../homework.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        with open('hw5.sql') as hw5_file:
            queries = hw5_file.readlines()
            for query in queries:
                result = cursor.execute(query.rstrip()).fetchall()
                response.append(result)
    print('number of students:')
    for i in response[0]:
        print(f'group:{i[0]}, number of students: {i[1]}')
    print('average score in groups: ')
    for i in response[1]:
        print(f'group:{i[0]}, average score: {i[1]}')
    print(f"\nNumber of students who failed to take the job: {response[2][0][0]}")
    print(f"Number of students who failed deadline: {response[3][0][0]}")
    print(f"number of repeat attempts: {response[4][0][0]}")