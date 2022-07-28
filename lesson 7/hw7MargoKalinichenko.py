"""
Знову апишіть программу "Касир в кінотеатрі", яка буде виконувати наступне:
Попросіть користувача ввести свсвій вік.
- якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"
- якщо користувачу менше 16 - вивести "Тобі лише <>, а це е фільм для дорослих!"
- якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
- якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!) - вивести "О, вам <>! Який цікавий вік!"
- у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів всеодно нема!"
Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік
Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача.
Наприклад :
"Тобі ж 5 років! Де твої батьки?"
"Вам 81 рік? Покажіть пенсійне посвідчення!"
"О, вам 33 роки! Який цікавий вік!"
Зробіть все за допомогою функцій! Для кожної функції пропишіть докстрінг.
Не забувайте що кожна функція має виконувати тільки одне завдання і про правила написання коду.
"""

age = input("Enter your age: ")


def input_check(arg1):
    """
    Function for checking if entered value is valid: digit, less maximum, not zero
    :param arg1: input entered by user
    :return: 0 if not valid, arg1 if valid
    """
    max_age = 120
    if not arg1.isdigit():
        print("Не є числом!")
        return 0
    elif int(arg1) > max_age:
        print(f'Більше максимума {max_age}')
        return 0
    elif int(arg1) == 0:
        print("З днем народження!")
        return 0
    else:
        return arg1


result_input_check = input_check(age)


def age_word_changing(arg1):
    """
    Function for right writing words after years.
    :param arg1: input entered by user
    :return: year and right word after year
    """
    while result_input_check == arg1:
        int_arg = int(arg1)
        last_arg = int(arg1[-1])
        if len(arg1) == 1:
            if last_arg == 1:
                str_age = 'рік'
                return arg1, str_age
            elif last_arg == 2 or last_arg == 3 or last_arg == 4:
                str_age = 'роки'
                return arg1, str_age
            else:
                str_age = 'років'
                return arg1, str_age
        elif len(arg1) > 1:
            prelast_arg = int(arg1[-2])
            if prelast_arg == 1:
                str_age = 'років'
                return arg1, str_age
            elif prelast_arg !=1:
                if last_arg == 1:
                    str_age = 'рік'
                    return arg1, str_age
                elif last_arg == 2 or last_arg == 3 or last_arg == 4:
                    str_age = 'роки'
                    return arg1, str_age
                else:
                    str_age = 'років'
                    return arg1, str_age
        break


result_word_changing = age_word_changing(age)


def message_output(tuple1):
    """
    Function for showing certain message depending from the year.
    :param tuple1: pair of year and word from function 'age_word_changing'
    :return: no return, just print needed message
    """
    while type(result_word_changing) == tuple:
        arg1 = tuple1[0]
        str1 = tuple1[1]
        if (len(arg1) > 1) and arg1.count(arg1[0]) == len(arg1):
            print(f'О, вам {arg1} {str1}! Який цікавий вік!')
        elif (int(arg1) < 7):
            print (f'Тобі ж {arg1} {str1}! Де твої батьки?')
        elif (int(arg1) < 16):
            print(f'Тобі лише {arg1} {str1}, а це фільм для дорослих!')
        elif (int(arg1) >= 65):
            print(f'Вам {arg1} {str1}? Покажіть пенсійне посвідчення!')
        else:
            print(f'Незважаючи на те, що вам {arg1} {str1}, білетів все одно немає!')
        break


result_message = message_output(result_word_changing)
