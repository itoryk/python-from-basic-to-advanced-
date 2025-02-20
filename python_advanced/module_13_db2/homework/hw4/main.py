import sqlite3

SALARY = 100000


def ivan_sovin_the_most_effective(
        cursor: sqlite3.Cursor,
        name: str,
) -> None:
    response = cursor.execute(f"SELECT salary FROM table_effective_manager WHERE name='{name}'")
    result = response.fetchone()[0]
    check_salary = result + (result / 10)
    if check_salary < SALARY:
        cursor.execute(f"UPDATE table_effective_manager SET salary = {int(check_salary)} WHERE name='{name}'")
        print('Зарплата повышена на 10%.')
    else:
        cursor.execute(f"DELETE FROM table_effective_manager WHERE name='{name}'")
        print('Сотрудник уволен.')


if __name__ == '__main__':
    name: str = input('Введите имя сотрудника: ')
    with sqlite3.connect('../homework.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        ivan_sovin_the_most_effective(cursor, name)
        conn.commit()
