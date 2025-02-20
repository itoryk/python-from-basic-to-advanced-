from typing import Any
import datetime
from datetime import datetime


class Date:
    @classmethod
    def from_string(cls, input_date: str) -> Any:
        convert = datetime.strptime(input_date, '%d-%m-%Y')
        print(f'День: {convert.day}\tМесяц: {convert.month}\tГод: {convert.year}')

    @classmethod
    def is_date_valid(cls, input_date: str) -> bool:

        try:
            datetime.strptime(input_date, '%d-%m-%Y')
            return True

        except ValueError:
            return False


date = Date.from_string('10-12-2077')
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))