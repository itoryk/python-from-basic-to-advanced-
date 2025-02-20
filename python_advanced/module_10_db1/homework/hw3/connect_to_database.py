import sqlite3
if __name__ == "__main__":
    with sqlite3.connect("hw_3_database.db") as conn:
        cursor = conn.cursor()

        for number in range(1, 4):
            table1_rows = cursor.execute(f"SELECT COUNT(*) FROM table_{number}")
            result = table1_rows.fetchall() [0][0]
            print(f"в {number} таблице {result} строк.")

        unique_rows = cursor.execute(f"SELECT_COUNT(*) FROM table_{number}")
        result2 = unique_rows.fetchall()[0][0]
        print(f"уникальных записей {result2}")

        t1_t2 = cursor.execute("SELECT COUNT(*) FROM table_1 t1 JOIN table_2 t2 ON  t1.id = t2.id")
        result3 = t1_t2.fetchall()[0][0]
        print(f'кол-во совпадающих записей {result3}')

        t1_t2_t3 = cursor.execute("SELECT COUNT(*) FROM table_1 t JOIN table_2 t1 ON  t.id = t1.id JOIN table_3 t2 ON t.id = t2.id")
        result4 = t1_t2_t3.fetchall()[0][0]
        print(f"кол-во совпадающих записей во всех таблицах {result4}")