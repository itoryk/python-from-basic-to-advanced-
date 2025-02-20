import sqlite3

if __name__ == "__main__":
    with sqlite3.connect("hw_1_database.db") as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM `table_car`")
        cursor.execute('INSERT INTO table_car (car_number, name, description, belongs_to) VALUES("К886УН68","Lada", "Клиент жаловался на тёмные выхлопы при езде в городе", 11)')
        cursor.execute('INSERT INTO table_car (car_number, name, description, belongs_to) VALUES("Н045МО97", "Lada", "Разбита левая фара, помят передний бампер", 12)')
        cursor.execute('INSERT INTO table_car (car_number, name, description, belongs_to) VALUES("Т682КО777", "Alfa Romeo", "Поменять резину на зимнюю. Царапина на капоте (?)", 13)')
        cursor.execute('INSERT INTO table_car (car_number, name, description, belongs_to) VALUES("О147НМ78", "Chevrolet", "Провести ТО №9", 14)')
        cursor.execute('INSERT INTO table_car (car_number, name, description, belongs_to) VALUES("К110ТА77", "Lada", "Развал-схождение + замена резины", 15)')
        cursor.execute('INSERT INTO table_car (car_number, name, description, belongs_to) VALUES("Е717ОЕ78", "Chevrolet" , "Помята водительская дверь, заменить габаритки", 16)')
        cursor.execute('INSERT INTO table_car (car_number, name, description, belongs_to) VALUES("У261ХО57", "Ford", "Заменить резину, проверить свечи ", 17)')
        cursor.execute('INSERT INTO table_car (car_number, name, description, belongs_to) VALUES("М649ОМ78", "Alfa Romeo", "Непонятные шумы при заводе", 18)')
        cursor.execute('INSERT INTO table_car (car_number, name, description, belongs_to) VALUES("С253НО90",  "Ford", "Заменить аккумулятор, проверить свечи", 19)')
        cursor.execute('INSERT INTO table_car (car_number, name, description, belongs_to) VALUES("А757АХ11", "Nissan", "ТО, клиент жалуется, что машину косит влево ", 20)')

        conn.commit()
        result = cursor.fetchall()

        print(result)
