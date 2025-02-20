"""
Довольно неудобно использовать встроенный валидатор NumberRange для ограничения числа по его длине.
Создадим свой для поля phone. Создайте валидатор обоими способами.
Валидатор должен принимать на вход параметры min и max — минимальная и максимальная длина,
а также опциональный параметр message (см. рекомендации к предыдущему заданию).
"""

from typing import Optional
from wtforms import IntegerField
from flask_wtf import FlaskForm
from wtforms import Field
from wtforms.validators import InputRequired, ValidationError


def number_length(form: FlaskForm, field: Field):
    min_len = 10
    max_len = 11

    if len(str(field.data)) < min_len or len(str(field.data)) > max_len:
        raise ValidationError


number = IntegerField(validators=[InputRequired(), number_length])


class NumberLength:
    def __init__(self, min_len: 10, max_len: 11):
        self.min_len = min_len
        self.max_len = max_len

    def __call__(self, form: FlaskForm, field: Field, message: Optional[str] = None):
        if len(str(field.data)) < self.min_len or len(str(field.data)) > self.max_len:
            return f"Invalid input, {form.errors}", 400


number2 = IntegerField(validators=[InputRequired(), NumberLength(min_len=10, max_len=11)])



