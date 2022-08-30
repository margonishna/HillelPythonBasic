import datetime


class Human:
    population = 0

    def __init__(self, name, surname, sex):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.__birth_date = datetime.datetime(2001, 5, 17)
        self.__class__.increase_population()

    @property
    def age(self):
        return (datetime.datetime.today() - self.__birth_date).days // 365

    @classmethod
    def increase_population(cls):
        print('New person was born')
        cls.population += 1


    def eat(self):
        print(f'I\'m eating, {self.name}')

    def __del__(self):
        print(f'{self.name} died')


man = Human('mjgjh', 'jhfhj', 'ngchg')
man1 = Human('mjgjh', 'jhfhj', 'ngchg')
man2 = Human('mjgjh', 'jhfhj', 'ngchg')
man3 = Human('mjgjh', 'jhfhj', 'ngchg')
print(man.age)
print(man.name)
print(Human.population)
print(man.population)

while man3:
    print(1)
    print(1)
