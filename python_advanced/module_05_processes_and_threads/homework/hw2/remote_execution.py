"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, что исполнение кода не уложилось в данное время.
"""
import shlex
import subprocess

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(validators=[InputRequired(), NumberRange(min=0, max=30)])


def run_python_code_in_subproccess(code: str, timeout: int):
    command = f"prlimit --nproc=1:1 python3 -c '{code}'"
    command = shlex.split(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    was_killed_by_timeout = False
    try:
        outs, errs = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        process.kill()
        outs, errs = process.communicate()
        was_killed_by_timeout = True
    return outs.decode(), errs.decode(), was_killed_by_timeout


@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()
    if form.validate_on_submit():
        code, timeout = form.code.data, form.timeout.data
        stdout, stderr, killed = run_python_code_in_subproccess(
            code=code, timeout=timeout)
        return f"Stdout: {stdout}, stderr: {stderr},process was killed by timeout: {killed}"
    return f"Bad request. Error, {form.errors}", 400


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
