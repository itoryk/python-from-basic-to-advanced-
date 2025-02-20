class Property():

    def __init__(self, worth):
        self.worth = worth

    def calculate_tax(self):
        pass


class Apartment(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth * (1 / 1000)


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth * (1 / 200)


class CountryHouse(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth * (1 / 500)


def calculate_total_tax(money, properties):
    total_tax = 0
    for property in properties:
        tax = property.calculate_tax()
        total_tax += tax
    return total_tax


def main():
    money = float(input("Введите количество ваших денег: "))

    apartment_worth = float(input("Введите стоимость квартиры: "))
    car_worth = float(input("Введите стоимость машины: "))
    country_house_worth = float(input("Введите стоимость дачи: "))

    apartment = Apartment(apartment_worth)
    car = Car(car_worth)
    country_house = CountryHouse(country_house_worth)

    properties = [apartment, car, country_house]

    total_tax = calculate_total_tax(money, properties)

    print(f"Налог на квартиру: {apartment.calculate_tax()}")
    print(f"Налог на машину: {car.calculate_tax()}")
    print(f"Налог на дачу: {country_house.calculate_tax()}")

    if total_tax > money:
        difference = total_tax - money
        print(f"Вам не хватает {difference} денег")
    else:
        print("У вас достаточно денег для оплаты налогов")


main()

