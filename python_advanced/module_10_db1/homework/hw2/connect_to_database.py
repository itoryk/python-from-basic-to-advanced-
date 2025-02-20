import sqlite3

if __name__ == "__main__":
    with sqlite3.connect("hw_2_database.db") as conn:
        cursor = conn.cursor()

        cursor.execute(
           'SELECT phone_id, COUNT(phone_id) FROM table_checkout tc Group by phone_id ORDER by COUNT(*) DESC LIMIT 3'
        )

        most_popular_3 = cursor.fetchall()

        cursor.execute(
            'SELECT phone_id, COUNT(phone_id) FROM table_checkout tc Group by phone_id ORDER by COUNT(*) LIMIT 3'
        )

        most_unpopular_3 = cursor.fetchall()

        cursor.execute(f"SELECT colour FROM table_phones tp WHERE id in ("
                       f"{most_popular_3[0][0]}, {most_popular_3[1][0]}, {most_popular_3[2][0]})")

        count_blue = 0
        count_red = 0
        colours = cursor.fetchall()
        for color in colours:
            if color[0] == "синий":
                count_blue += 1
            elif color[0] == "красный":
                count_red += 1
        if count_blue > count_red:
            print('Синий цвет самый популярный')
            print(f"В тройке лидеров {count_blue} - синих и {count_red} - красных")
        else:
            print("Красный цвет самый популярный")

        cursor.execute(f"SELECT colour FROM table_phones tp WHERE id={most_unpopular_3[0][0]}")
        unpopular_colour = cursor.fetchall()
        print(f"наименее популярный цвет - {unpopular_colour[0][0]}, "
              f"{most_unpopular_3[0][1]} штук продано")

