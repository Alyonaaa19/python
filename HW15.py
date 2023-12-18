import random


class Car:

    def __init__(self, color, model, economy: int, mileage: int = 0, fuel: int = 100):
        self._mileage = mileage
        self._fuel = fuel
        self._economy = economy
        self._color = color
        self._model = model

    def get_mileage(self):
        return f"Your car mileage is {self._mileage}"

    def get_fuel(self):
        return f"Your car fuel is {self._fuel}"

    def get_economy(self):
        return f"Your car economy is {self._economy}"

    def get_color(self):
        return f"Your car color is {self._color}"

    def get_model(self):
        return f"Your car model is {self._model}"

    def set_mileage(self, mileage):
        self._mileage = mileage

    def set_fuel(self, fuel):
        self._fuel = fuel

    def set_economy(self, economy):
        self._economy = economy

    def set_color(self, color):
        self._color = color

    def set_model(self, model):
        self._model = model

    def drive(self, distance):
        if distance > self.distance_left():
            raise Exception("Не вистачає палива")
        else:
            self._mileage += distance
            self._fuel -= distance / 100 * self._economy

    def distance_left(self):
        return self._fuel / self._economy * 100

    def fuel_up(self):
        self._fuel += 20


list_models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
list_cars_color = ["Black", "White", "Orange", "Blue", "Green"]
list_cars_economy = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
list_cars = []

for i in range(10):
    car = Car(random.choice(list_cars_color), random.choice(list_models), random.choice(list_cars_economy))
    list_cars.append(car)

for car in list_cars:
    car.drive(200)
    car.fuel_up()
    car.drive(100)

car = max(list_cars, key=lambda c: c.get_fuel())
print(f"{car.get_model()}, {car.get_color()} {car.get_economy()}, {car.get_fuel()}, {car.get_mileage()}")