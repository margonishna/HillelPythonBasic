from random import randint


def get_number_from_user():
    """
    Пропонує ввести значення і перевіряє введене значення
    :return: Повертає 1,2 чи 3 в залежності від введенного значення
    """
    print('Щоб зіграти з компьютером у гру \'Камінь Ножиці Папір\' оберіть одну з опцій: 1 - Камінь, 2 - Ножиці, 3 - Папір')
    while True:
        my_str = input("Введіть одну з цифр - 1, 2 або 3: ")
        if not my_str.isdigit():
            print("Не є числом. Введіть одну з цифр - 1, 2 або 3:")
            continue
        elif int(my_str) != 1 and int(my_str) != 2 and int(my_str) != 3:
            print("Ви ввели не вірне число. Введіть одну з цифр - 1, 2 або 3:")
            continue
        elif int(my_str) == 1:
            print("Ви обрали Камінь!")
            return int(my_str)
        elif int(my_str) == 2:
            print("Ви обрали Ножиці!")
            return int(my_str)
        elif int(my_str) == 3:
            print("Ви обрали Папір!")
            return int(my_str)
        break


def get_number_from_computer():
    """
    Комп'ютер обирає значення і прінт показує що обрав комп'ютер
    :return: Повертає 1,2 чи 3 в залежності від обранного значення
    """
    number_comp = randint(1, 3)
    if number_comp == 1:
        print("Комп'ютер обрав Камінь!")
        return number_comp
    elif number_comp == 2:
        print("Комп'ютер обрав Ножиці!")
        return number_comp
    elif number_comp == 3:
        print("Комп'ютер обрав Папір!")
        return number_comp


def game_logic(user_number, computer_number):
    """
    Порівняння обраних значень від ігрока та комп'ютера
    :param user_number: Значення що обрав ігрок
    :param computer_number: Значення що обрав комп'ютера
    :return: 0 - коли нічия, 10 - коли виграв ігрок, 20 - коли виграв комп'ютер
    """
    if user_number == 1:
        if computer_number == 1:
            return 0
        elif computer_number == 2:
            return 10
        elif computer_number == 3:
            return 20
    elif user_number == 2:
        if computer_number == 1:
            return 20
        elif computer_number == 2:
            return 0
        elif computer_number == 3:
            return 10
    elif user_number == 3:
        if computer_number == 1:
            return 10
        elif computer_number == 2:
            return 20
        elif computer_number == 3:
            return 0


def who_won():
    """
    Передаємо значення які були обрані ігроком та комп'ютером, дізнаємось результат функції порівняння game_logic
    :return: 'equal' якщо нічия, 'user' якщо ігрок виграв, 'comp' якщо комп'ютер
    """
    user_number = get_number_from_user()
    computer_number = get_number_from_computer()
    if game_logic(user_number, computer_number) == 0:
        print("Нічия!")
        return 'equal'
    elif game_logic(user_number, computer_number) == 10:
        print("Ви виграли!!!")
        return 'user'
    elif game_logic(user_number, computer_number) == 20:
        print("Комп'ютер виграв!")
        return 'comp'


def ask_to_continue():
    """
    Функція питає ігрока чи він хоче продовжити, перевіряє що він ввів
    :return: 'Yes' or 'No'
    """
    while True:
        print("Чи бажаете продовжити гру?")
        my_str = input("Введіть одну з букв для відповіді: Y - так, N - ні: ")
        if my_str == 'Y':
            return 'Yes'
        elif my_str == 'N':
            return 'No'
        else:
            print("Неправильний ввод.")
            continue


def victory_counter(victories_counter, winner):
    """
    Функція, що добавляє значення до ключа 'user' якщо виграв ігрок, або до ключа 'comp' якщо виграв комп'ютер
    :param victories_counter: Дікт, в якому записується результат ігр
    :param winner: Переможець з фунції who_won
    :return: Дікт, в якому записується результат гри
    """
    if winner != 'equal':
        if winner == 'user':
            victories_counter['user score'] += 1
            return victories_counter
        else:
            victories_counter['computer score'] += 1
            return victories_counter


def game():
    """
    Запускає гру, запускає лічильник гри, запускає функцію що питає ігрока чи продовжити гру
    :return:
    """
    victories_counter = {'user score': 0, 'computer score': 0}
    while True:
        winner = who_won()
        victory_counter(victories_counter, winner)
        user_answer = ask_to_continue()
        print(victories_counter)
        if user_answer == 'Yes':
            continue
        else:
            break
