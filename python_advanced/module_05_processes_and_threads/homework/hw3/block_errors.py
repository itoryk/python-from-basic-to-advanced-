"""
Реализуйте контекстный менеджер, который будет игнорировать переданные типы исключений, возникающие внутри блока with.
Если выкидывается неожидаемый тип исключения, то он прокидывается выше.
"""

from typing import Collection, Type, Literal
from types import TracebackType

err_types = {ZeroDivisionError, TypeError}


class BlockErrors:
    def __init__(self, errors: Collection) -> None:
        self.errors = errors

    def __enter__(self) -> None:
        ...

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        if issubclass(exc_type, tuple(self.errors) or exc_type in self.errors):
            return True


if __name__ == '__main__':
    with BlockErrors(err_types):
        a = 1/0
    print('Success')