from abc import ABC, abstractmethod
import enum
import random
import time
import sys

# import winsound


class Constants(enum.Enum):
    MAX_HEALTH_POINTS = 100
    INIT_MONEY = 1000
    INIT_HEALTH = 100
    INIT_DAMAGE_POWER = 50
    INIT_DEFENCE_POWER = 50


class Price(enum.Enum):
    DAMADE = 25
    DEFENCE = 50


class Color(enum.Enum):
    """dh"""
    RED = '\033[33m{}\033[0m'


class Hero(ABC):

    def _setup(self):
        self.max_health_points = Constants.MAX_HEALTH_POINTS.value
        self.money = Constants.INIT_MONEY.value
        self.health = Constants.INIT_HEALTH.value
        self.damage_power = Constants.INIT_DAMAGE_POWER.value
        self.defence_power = Constants.INIT_DEFENCE_POWER.value

    def attack(self, other):
        if not random.randint(0, 100) < self.accuracy:
            print(f'{self.name} missed')
            return
        else:
            # winsound.Beep(500, 1000)
            if self.damage_power <= other.defence_power:
                pass
            else:
                other.health = other.health - self.damage_power + other.defence_power

        if other.health < 0:
            other.health = 0

        if not other.is_alive:
            print(f'{self.name} won the battle')
            time.sleep(3)
            sys.exit()

    def rise_damage_power(self):
        print(f'You have {self.money} dollars')
        if self.money > Price.DAMADE.value:
            print(f'You can buy only {int(self.money/Price.DAMADE.value)} damage points')
            command = input('Enter 1 if you want to buy, other key to exit >>> ')

            if command == '1':
                possible_rise_damage = int(input('Enter quantity you want >>> '))
                if possible_rise_damage > int(self.money/Price.DAMADE.value):
                    print("incorrect quantity")
                    return self

                self.damage_power += possible_rise_damage
                self.money -= possible_rise_damage * Price.DAMADE.value
        else:
            print('You have not enough money to buy')
        return self

    def rise_defence_power(self):
        print(f'You have {self.money} dollars')
        if self.money > Price.DEFENCE.value:
            print(f'You can buy only {int(self.money / Price.DEFENCE.value)} damage points')
            command = input('Enter 1 if you want to buy, other key to exit >>> ')

            if command == '1':
                possible_rise_damage = int(input('Enter quantity you want >>> '))
                if possible_rise_damage > int(self.money / Price.DEFENCE.value):
                    print("incorrect quantity")
                    return self

                self.damage_power += possible_rise_damage
                self.money -= possible_rise_damage * Price.DEFENCE.value
        else:
            print('You have not enough money to buy')
        return self

    @abstractmethod
    def __str__(self):
        pass

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Hero):
    def __init__(self, name):
        self.name = name
        self._setup()
        self.damage_power += random.randint(20, 30)
        self.accuracy = random.randint(20, 30)

    def __str__(self):
        return f'Character {self.name} is a {self.__class__.__name__}; health {self.health}pt,' \
               f'damage power {self.damage_power}pt, defence power {self.defence_power}pt, ' \
               f'accuracy {self.accuracy}'

    __repr__ = __str__


class Archer(Hero):
    def __init__(self, name):
        self.name = name
        self._setup()
        self.damage_power += random.randint(15, 20)
        self.accuracy = random.randint(50, 80)

    def __str__(self):
        return f'Character {self.name} is a {self.__class__.__name__}; health {self.health}pt,' \
               f'damage power {self.damage_power}pt, defence power {self.defence_power}pt, ' \
               f'accuracy {self.accuracy}'

    __repr__ = __str__

class Battle:

    @staticmethod
    def main_battle(player1: Hero, player2: Hero):
        if player1 == player2:
            raise ValueError('KAMICADZE')

        while True:
            player1.attack(player2)
            player2.attack(player1)


if __name__ == '__main__':
    a1 = Archer('1111')
    k2 = Knight('2222')

    archers = []

    for ar in range(0, 1000000):
        archers.append(Archer(f'Number {ar}'))


    new_battle = Battle()
    new_battle.main_battle(archers[0], k2)

