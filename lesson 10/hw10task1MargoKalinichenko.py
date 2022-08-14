"критерієм перевірки буде проходження всіх ассертів"

##############################################################################
############                                                     #############
############                      TASK 1                         #############
############                                                     #############
##############################################################################
"""
написати декоратор wrap_validate, який не приймає жодних параметрів
його задача - перевірити, що функція, яку він задекорував, обовязково отримала
в своїх аргументах параметр 'password' (згадуємо про * в написанні аргументів функції)
значення 'password' повинне бути стрічкою, довжиною не менше 10 символів,
та містити в собі латинські літери (регістр не принципово), арабські цифри та знак '!"

кожну з перевірок отриманого значення паролю виконуємо в ОКРЕМІЙ функції, функції робимо
універсальними, називаємо їх (з опційними параметрами)
- is_valid_length(length=10)
- has_any_symbols(symbols='qwertyuiopasdfghjklzxcvbnm') (це приклад для латинських букв, повертає тру, якщо хоч
один символ в стрічці, аналогічно зробити для цифр та знаку оклику (у вас буде 3 виклики функції в середині декоратора
з різними параметрами)
- is_string()

якщо  'password'  відсутній - викликаємо помилку
raise AttributeError(f'no parameter "password" in arguments of function{func.__name__}')

якщо  'password'  не задовольняє вимогам валідації, написаним вище, то повертається словник виду
{ 'result': str(func(*args, **kwargs)),
  'is_secure': False,
}

якщо  'password'  задовольняє вимогам валідації, написаним вище, то повертається словник виду
{ 'result': str(func(*args, **kwargs)),
  'is_secure': True,
}

зауважте, що str(func(*args, **kwargs)) МАЄ бути довжиною не більше 100 символів
якщо даний результат буде довшим за 100 символів, то стрічка має бути обрізана до 100 символів, причому останні
три символи мають бути ... (трьома крапками)
тут ви вже й самы здогадалися написати функцію на виконання даної роботи (тут вже без підказок)
"""

import datetime


def is_valid_length(value, length=10):
    return False if len(str(value)) < length else True


def has_any_symbols(value):
    for i in str(value):
        if not i.isalpha():
            continue
        return True


def has_any_numbers(value):
    for i in str(value):
        if not i.isdigit():
            continue
        return True


def has_any_marks(value):
    for i in str(value):
        if not i == '!':
            continue
        return True


def is_string(value):
    return False if not type(value) == str else True


def str_more_100(value, length=100):
    list1 = list(value)
    str_length = len(str(value))
    if str_length > length:
        list1[101] = '.'
        list1[102] = '.'
        list1[103] = '.'
        return ''.join(list1[0:104]).strip(',')
    else:
        return value


def wrap_validate(func):
    def check_password(*args, **kwargs):
        if not 'password' in kwargs:
            raise AttributeError(f'no parameter "password" in arguments of function{func.__name__}')

        password_value = kwargs['password']
        check1 = is_valid_length(password_value)
        check2 = has_any_symbols(password_value)
        check3 = has_any_marks(password_value)
        check4 = is_string(password_value)

        func_result = str_more_100(str(func(*args, **kwargs)))

        if check1 and check2 and check3 and check4 is True:
            return print({'result': func_result,
                          'is_secure': True})
        return print({'result': func_result,
                      'is_secure': False})
    return check_password


@wrap_validate
def registration(id_user, login, notes, *, password):
    date = datetime.date.today()
    return f'User {login} created account on {date} with password "{password}". Additional information: {notes}'


if __name__ == '__main__':
    registration(56, 'user_name', 'hi', password=7897)
    # registration(8439, 'Lola', 'she is new', password='')
    # registration(8434, 'Kagura', 'she is new', dfsfd='')
    registration(839, 'Jason', 'this is very long notes', password='hhjkhjyijhkj23!')
    # registration(458, 'Lola', 'she is new', password='hhjkhjyijhkj23!')
    # assert is_valid_length(10), 'not valid length'
    # assert is_valid_length(1234567890)
    # assert has_any_symbols('qwertyuiopasdfghjklzxcvbnm')
    # assert has_any_symbols(678), "doesn't have symbols"
    # assert has_any_symbols('!6asdf')
    # assert has_any_numbers('fdsfs'), "doesn't have numbers"
    # assert has_any_marks('fdsfs'), "doesn't have '!'"
    # assert has_any_marks('fd!sfs')
    # assert is_string(5454), "not str"
    # assert is_string('45')
