"""
Створити клас Vehicle (транспортний засіб):
ні від чого не наслідується
в ініціалізатор класу (__init__ метод) передати
producer: str
model: str
year: int
tank_capacity: float # обєм паливного баку
tank_level: float = 0 # початковий параметр рівня паливного баку дорівнює 0, параметр в аргументах не передавати
maxspeed: int
fuel_consumption: float # litres/100km споживання пального
odometer_value: int = 0 # при сході з конвеєра пробіг нульовий, параметр в аргументах не передавати

визначити метод __repr__, яким повертати інформаційну стрічку (наповнення на ваш вибір,
проте параметри model and year and odometer_value мають бути передані

написати метод refueling, який не приймає жодного аргумента,
заправляє автомобіль на уявній автозаправці до максимума (tank_level = tank_capacity),
 після чого виводить на екран повідомлення, скільки літрів було заправлено
 (перша заправка буде повного баку, а в інших випадках величина буде залежати від залишку пального в баку)

написати метод race, який приймає один аргумент (не враховуючи self) - відстань,
яку потрібно проїхати, а повертає словник, в якому вказано, скільки авто проїхало,
з огляду на заповнення паливного баку перед поїздкою, залишок пального (при малому кілометражі все пальне не використається),
та час, за який відбулася дана поїздка, з урахування, що середня швидкість складає 80% від максимальної
(витрата пального рівномірна незалежно від швидкості)
за результатами роботи метода в атрибуті tank_level екземпляра класа має зберігатися залишок пального після поїздки
(зрозуміло, що не менше 0)
збільшити на величину поїздки показники odometer_value

написати метод lend_fuel, який приймає окрім self ще й other обєкт, в результаті роботи якого паливний бак обєкта,
на якому було викликано відповідний метод, наповнюється до максимального рівня за рахунок відповідного зменшення рівня
пального у баку дружнього транспортного засобу
вивести на екран повідомлення з текстом типу "Дякую, бро, виручив. Ти залив мені *** літрів пального"
у випадку, якщо бак першого обєкта повний або у другого обєкта немає пального, вивести повідомлення "Нічого страшного, якось розберуся"

написати метод __eq__, який приймає окрім self ще й other обєкт (реалізація магічного методу для оператора порівняння == )
даний метод має повернути True у випадку, якщо 2 обєкта, які порівнюються, однакові за показниками року випуску та пробігу
(значення відповідних атрибутів однакові, моделі можуть бути різними)

створіть не менше 2-х обєктів класу, порівняйте їх до інших операцій, заправте їх, покатайтесь на них на різну відстань,
перевірте пробіг, позичте один в одного пальне, знову порівняйте
"""


class Vehicle:
    """
    Class which creats objects with transport arguments: producer, model, year, tank capacity, max speed, fuel consumption,
    tank level and odometer value
    """
    tank_level = 0
    odometer_value = 0

    def __init__(self, producer: str, model: str, year: int, tank_capacity: float, max_speed: int,
                 fuel_consumption: float):
        self.producer = producer
        self.model = model
        self.year = year
        self.tank_capacity = tank_capacity
        self.max_speed = max_speed
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f'Car model is {self.model} {self.year} year, mileage is {self.odometer_value} kms, ' \
               f'fuel consumption is {self.fuel_consumption} litres. ' \
               f'Current tank level is {self.tank_level} litres and tank capacity is {self.tank_capacity} litres.'

    __repr__ = __str__

    def refueling(self):
        """
        Fills tank of the car to maximum value - tank_capacity. Prints how much litres were filled in car's tank.
        :return: updated tank_level, which should be equal to tank_capacity
        """
        if self.tank_level == 0:
            print('Car was fueled with', self.tank_capacity, 'litres')
        else:
            litres_was_fueled = self.tank_capacity - self.tank_level
            print('Car was fueled with', litres_was_fueled, 'litres')
        self.tank_level = self.tank_capacity
        return self.tank_level

    def race(self, road_length):
        """
        Makes car to start trip for certain road_length. Max_road_length is counted by current tank_level
        and fuel_consumption of the car.
        If max_road_length is 0, trip won't happen, if road_length is equal or less than max_road_length,
        trip will happen. In other cases trip will happen partly until fuel will end.
        :param road_length: road length, which car should pass
        :return: dict with all changed parameters
        """
        max_road_length = self.tank_level / self.fuel_consumption * 100
        time_trip = road_length / (0.8 * self.max_speed)
        time_trip = round(time_trip, 1)

        if max_road_length == 0:
            road_length = 0
            time_trip = 0
        elif road_length <= max_road_length:
            needed_fuel = road_length * self.fuel_consumption / 100
            self.tank_level = self.tank_level - needed_fuel
            self.odometer_value += road_length
        else:
            self.tank_level = 0
            road_length = max_road_length
            self.odometer_value += road_length

        dict_road = {'How many kms car has passed in this trip': road_length,
                     'How many kms car has passed generally': self.odometer_value,
                     'How many fuel has left': self.tank_level,
                     'How much hours were spent for the trip': time_trip}
        print(dict_road)
        return dict_road

    def lend_fuel(self, other):
        """
        Car lens fuel from other car. If current car doesn't need fuel or other car doesn't have fuel - lending won't happen.
        If other car has all fuel to share - fuel will be shared how much is needed.
        If other has some fuel to share - it will be shared and tank of other car will become empty.
        :param other: other car
        :return: how much fuel was shared
        """
        needed_fuel = self.tank_capacity - self.tank_level
        fuel_shared = 0

        if needed_fuel == 0 or other.tank_level == 0:
            print('No problems, will figure this out.')
        elif needed_fuel <= other.tank_level:
            fuel_shared = needed_fuel
            self.tank_level += fuel_shared
            other.tank_level -= fuel_shared
            print(f"Thanks, bro! You've shared with me {fuel_shared}")
        elif needed_fuel > other.tank_level:
            fuel_shared = other.tank_level
            self.tank_level += fuel_shared
            other.tank_level = 0
            print(f"Thanks, bro! You've shared with me {fuel_shared}")
        return fuel_shared

    def __eq__(self, other):
        if self.year == other.year and self.odometer_value == other.odometer_value:
            return True
        return False


if __name__ == '__main__':
    lamborghini1 = Vehicle('Automobili Lamborghini S.p.A.', 'Lamborghini Jalpa', 1982, 60, 250, 15)
    print(lamborghini1)
    lamborghini1.race(100)
    lamborghini1.refueling()
    print(lamborghini1)
    lamborghini1.refueling()
    lamborghini1.race(100)
    lamborghini1.refueling()
    lamborghini1.race(1000)
    print(lamborghini1)
    lamborghini1.refueling()
    lamborghini1.race(250)
    print('=' * 160)

    lamborghini2 = Vehicle('Automobili Lamborghini S.p.A.', 'Lamborghini Diablo', 2001, 80, 325, 20)
    print(lamborghini2)
    print('=' * 160)

    lamborghini3 = Vehicle('Automobili Lamborghini S.p.A.', 'Lamborghini Murciélago', 2001, 70, 342, 32)
    print(lamborghini3)
    print('=' * 160)

    # Sharing fuel
    print('lamborghini1 tank level:', lamborghini1.tank_level)
    print('lamborghini2 tank level:', lamborghini2.tank_level)
    lamborghini1.lend_fuel(lamborghini2)
    print('=' * 160)

    lamborghini1.refueling()
    lamborghini1.lend_fuel(lamborghini2)
    print('lamborghini1 tank level:', lamborghini1.tank_level)
    print('lamborghini2 tank level:', lamborghini2.tank_level)
    print('=' * 160)

    lamborghini2.lend_fuel(lamborghini1)
    print('lamborghini1 tank level:', lamborghini1.tank_level)
    print('lamborghini2 tank level:', lamborghini2.tank_level)
    print('=' * 160)

    lamborghini2.race(100)
    lamborghini1.refueling()
    print('lamborghini1 tank level:', lamborghini1.tank_level)
    print('lamborghini2 tank level:', lamborghini2.tank_level)
    lamborghini2.lend_fuel(lamborghini1)
    print('lamborghini1 tank level:', lamborghini1.tank_level)
    print('lamborghini2 tank level:', lamborghini2.tank_level)
    print('=' * 160)

    # Comparisons
    print(lamborghini1)
    print(lamborghini2)
    print('lamborghini1 == lamborghini2:', lamborghini1 == lamborghini2)
    print('=' * 160)

    lamborghini3.refueling()
    lamborghini3.race(100)
    print(lamborghini2)
    print(lamborghini3)
    print('lamborghini2 == lamborghini3:', lamborghini2 == lamborghini3)
