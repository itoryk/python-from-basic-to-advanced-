from typing import Callable, Any
import math


class MyMath:

    def display(func: Callable) -> Any:
        def wrapper(*args, **kwargs):   #обёртка для красивого вывода
            resalt = func(*args, **kwargs)
            print(f'Резултат работы функции {func.__name__}: {resalt}' )
            return func
        return wrapper

    @classmethod
    @display
    def circle_len(cls, radius: Any) -> float:   #длина окружности
        a = round(2 * math.pi * radius, 3)
        return a

    @classmethod
    @display
    def circle_sq(cls, radius: Any) -> float:    #площадь окружности
        s = round(math.pi * (radius ** 2), 3)
        return s

    @classmethod
    @display
    def cube_v(cls, len: Any) -> int:    #объём куба
        v = len**3
        return v

    @classmethod
    @display
    def sphere_sq(cls, radius: Any) -> float:    #площадь поверхности сферы
        s = round(4 * math.pi * radius * 2, 3)
        return s


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_v(len=6)
res_4 = MyMath.sphere_sq(radius=6)

