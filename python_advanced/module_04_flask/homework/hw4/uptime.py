"""
Напишите GET-эндпоинт /uptime, который в ответ на запрос будет выводить строку вида f"Current uptime is {UPTIME}",
где UPTIME — uptime системы (показатель того, как долго текущая система не перезагружалась).

Сделать это можно с помощью команды uptime.
"""

from flask import Flask
import subprocess

app = Flask(__name__)


@app.route("/uptime", methods=['GET'])
def uptime() -> str:
    return f"Current uptime is {get_uptime()}"


def get_uptime():
    result = subprocess.run(['uptime', '-p'], capture_output=True, text=True)
    uptime_output = result.stdout.strip()

    return uptime_output.split(' ')[-1]


if __name__ == '__main__':
    app.run(debug=True)
