import sqlite3
import csv


def delete_wrong_fees(
        cursor: sqlite3.Cursor,
        wrong_fees_file: str
) -> None:
    with open('wrong_fees.csv') as wrong_fees:
        cars = csv.reader(wrong_fees)
        cars_num = []
        for num in cars:
            if num[0] != 'car_number':
                cars_num.append(num[0])
        cars_num_1 = tuple(cars_num)
        request = f"""
            DELETE FROM 'table_fees' WHERE truck_number IN {cars_num_1}
        """
        cursor.execute(request)
        print('DATA EXPUNGED')


if __name__ == "__main__":
    with sqlite3.connect("../homework.db") as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        delete_wrong_fees(cursor, "wrong_fees.csv")
        conn.commit()
