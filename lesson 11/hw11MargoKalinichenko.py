"""
Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від "Транспортний засіб".
Наповніть класи атрибутами на свій розсуд. Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".
"""


class Transport:
    name = None
    max_speed = None
    min_crew_number = None

    def __init__(self, name, max_speed, min_crew_number):
        self.name = name
        self.max_speed = max_speed
        self.min_crew_number = min_crew_number

    def print_all_attr(self):
        return f'Max speed of {self.name} is {self.max_speed} km/h, minimal crew number is {self.min_crew_number}.'


class Car(Transport):
    number_of_wheels = None

    def print_all_attr(self):
        return f'Max speed of {self.name} is {self.max_speed} km/h, minimal crew number is {self.min_crew_number}, ' \
               f'and number of wheels is {self.number_of_wheels}.'


class Plane(Transport):
    number_of_emergency_exits = None

    def print_all_attr(self):
        return f'Max speed of {self.name} is {self.max_speed} km/h, minimal crew number is {self.min_crew_number}, ' \
               f'and number of emergency exits is {self.number_of_emergency_exits}.'


class Ship(Transport):
    length_ship = None
    number_of_lifeboats = None

    def print_all_attr(self):
        return f'Max speed of transport is {self.max_speed} km/h, minimal crew number is {self.min_crew_number}, ' \
               f'and length of ship is {self.length_ship} m and number of lifeboats is {self.number_of_lifeboats}.'


lamborghini = Car('Lamborghini', 350, 1)
lamborghini.number_of_wheels = 4

boeing_737 = Plane('Boeing 737', 927, 6)
boeing_737.number_of_emergency_exits = 4

cruise_ship = Ship('Cruise ship', 40, 30)
cruise_ship.length_ship = 250
cruise_ship.number_of_lifeboats = 6

print(lamborghini.print_all_attr())
print(boeing_737.print_all_attr())
print(cruise_ship.print_all_attr())

