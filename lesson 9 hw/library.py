"""
Візьміть гру з заняття і доопрацюйте її наступним чином:
всі функції в окремий файл
додайте підказки привгадуванні:
(якщо різниця між числом користувача і загаданим більше 10 - вивести "Холодно",
якщо 5-10 - "Тепло", якщо 1-4 "Гаряче")
додайте можливість на початку програми вказати кількість спроб вгадування.
 користувач має вгадати число за вказану кількість спроб
Напишіть декоратор, який вимірює і виводить на екран час виконання функції в секундах
 і задекоруйте ним основну функцію гри. Після закінчення гри декоратор має сповістити, скільки тривала гра.
"""

import time
from random import randint


def get_random_number():
    """
    Returns:
        (int)
    """
    number = randint(1, 101)
    return number


def get_number_of_attempts():
    while True:
        try:
            return int(input("Попробуйте вгадати число, що загадала програма! Введіть кількість спроб: "))
        except:
            print("Це не ціле число.")


def get_number_from_user():
    """
    Returns:
        (int)
    """
    while True:
        try:
            return int(input("Введіть число, спробуйте вгадати що було загадано: "))
        except:
            print("Це не ціле число.")


def check_numbers(to_guess, user_number):
    """

    Args:
        to_guess (int):
        user_number (int):

    Returns:
        (bool):
    """
    print(f'---> {to_guess}')
    if to_guess == user_number:
        return True
    else:
        return False


def hint(arg1, arg2):
    if abs(arg1 - arg2) > 10:
        print("Холодно")
    elif 5 <= abs(arg1 - arg2) <= 10:
        print("Тепло")
    elif 1 <= abs(arg1 - arg2) <= 4:
        print("Гаряче")


def decorator_time_counter(func):
    def timecount():
        start = time.time()
        func()
        end = time.time()
        time_process = int(end - start)
        print(f'Час на виконання функції в секундах: {time_process}')
        # print(type(func()))
        # print(type(func))
        # print(type(time_process))
        return time_process

    return timecount


@decorator_time_counter
def game():
    number_of_attempts = get_number_of_attempts()
    number_to_guess = get_random_number()
    while number_of_attempts != 0:
        user_number = get_number_from_user()
        number_of_attempts -= 1
        hint(user_number, number_to_guess)
        if check_numbers(number_to_guess, user_number):
            print("Ви вгадали!!!!")
            break
        else:
            print("Ви не вгадали!")
            continue
