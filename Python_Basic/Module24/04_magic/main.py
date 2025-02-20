class Water:
    def __str__(self) -> str:
        return 'Вода'
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()


class Air:
    def __str__(self) -> str:
        return 'Воздух'

    def __add__(self, other):

        if isinstance(other, Fire):
            return Thunder()

        elif isinstance(other, Water):
            return Storm()

        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Fire:
    def __str__(self) -> str:
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Magma()

class Earth:
    def __str__(self) -> str:
        return 'Земля'


class Storm():
    def __str__(self) -> str:
        return 'Шторм'


class Vapor():
    def __str__(self) -> str:
        return 'Пар'


class Dirt():
    def __str__(self) -> str:
        return 'Грязь'


class Thunder():

    def __str__(self) -> str:
        return 'Молния'


class Dust():

    def __str__(self) -> str:
        return 'Пыль'


class Magma():

    def __str__(self) -> str:
        return 'Лава'


water = Water()

air = Air()

fire = Fire()

earth = Earth()

print(air + water, air + fire, fire + earth)
