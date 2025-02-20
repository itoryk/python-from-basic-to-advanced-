import random
import sqlite3

TEAMS = [
    ("Реал Мадрид", "Испания", "сильная"), ("Бавария", "Германия", "сильная"),
    ("Атлетико М", "Испания","сильная",), ("Барселона", "Испания", "сильная"),
    ("Марибор", "Словения","средняя"), ("Зенит", "Россия", "средняя"),
    ("Интер Милан", "Италия","средняя"), ("Байер Л", "Германия", "средняя"),
    ("Пхохан Стилерс", "Южная Корея", "слабая"), ("Абердин", "Шотландия", "слабая"),
    ("Виктория Пльзень", "Чехия", "слабая"), ("ЭС Сетиф", "Алжир", "слабая")]

TEAMS_LEVELS = ["сильная", "средняя", "слабая"]


def generate_test_data(
        cursor: sqlite3.Cursor,
        number_of_groups: int
) -> None:
    if not cursor.execute("SELECT EXISTS(SELECT * FROM uefa_commands)"):
        cursor.executemany(
            f"INSERT INTO uefa_commands (command_name, command_country, command_level) VALUES(?,?,?)", TEAMS
        )
    else:

        cursor.execute("DELETE FROM uefa_draw")

        for number in range(1, number_of_groups + 1):
            groups = []
            for i in TEAMS_LEVELS:
                response = cursor.execute(f"SELECT command_number FROM uefa_commands WHERE command_level='{i}'")
                comm_num = response.fetchall()

                if i == 1:
                    new_tuple = (number,)
                    new_tuple = new_tuple + random.choice(comm_num)
                    groups.append(new_tuple)

                new_tuple = (number,)
                new_tuple = new_tuple + random.choice(comm_num)
                groups.append(new_tuple)
            cursor.executemany("INSERT INTO uefa_draw (command_number, group_number) VALUES (?,?)", groups)


if __name__ == '__main__':
    number_of_groups: int = int(input('Введите количество групп (от 4 до 16): '))
    with sqlite3.connect('../homework.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        generate_test_data(cursor, number_of_groups)
        conn.commit()
