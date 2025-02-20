import sqlite3

if __name__ == "__main__":
    with sqlite3.connect("hw_4_database.db") as conn:
        cursor = conn.cursor()

        humans = cursor.execute("SELECT COUNT(*) FROM salaries s WHERE s.salary < 5000")
        result = humans.fetchall()[0][0]
        print(f"кол-во человек с острова N, находящихся за чертой бедности {result}")

        average_salary = cursor.execute("SELECT ROUND(AVG(salary), 2 ) FROM salaries")
        result_salary = average_salary.fetchall()[0][0]
        print(f"Средняя зп по острову N {result_salary}")

        median_salary = cursor.execute("""
            SELECT salary FROM (SELECT ROW_NUMBER () OVER (ORDER BY salary) RowNum,
            salary FROM salaries s) WHERE RowNum = (SELECT COUNT(*) / 2 + 1 FROM salaries s)
        """)
        result_median = median_salary.fetchall()[0][0]
        print(f"медийная зп по острову N {result_median}")

        social_inequality = cursor.execute("""
            SELECT ROUND(SUM(salary)* 1.0 / (SELECT SUM(salary) - (SELECT SUM(salary) FROM (SELECT * FROM salaries
            ORDER BY salary DESC LIMIT 0.1 * (SELECT COUNT(*) FROM salaries))) FROM salaries)  * 1.0, 2) FROM
            (SELECT * FROM salaries ORDER BY salary DESC LIMIT 0.1 * (SELECT COUNT(*) FROM salaries))
        """)
        result_social = social_inequality.fetchall()[0][0]
        print(f"число социального неравенства {result_social}")
