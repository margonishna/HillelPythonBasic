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

##############################################################################
############                                                     #############
############                      TASK 2                         #############
############                                                     #############
##############################################################################
"""
написати функцію registration, яка приймає
- позиційний аргумент id, стрічка або число - не важливо,  значення за замовчуванням - відсутнє
- позиційний або іменований аргумент login, тип даних - не важливий, значення за замовчуванням - відсутнє
- позиційний або іменований аргумент notes, тип даних - не важливий, значення за замовчуванням - відсутнє
- password - тип даних - не важливий, значення за замовчуванням - відсутнє

в середині функції вставити код (зназок для отримання даних прописаний нижче)
date = datetime.date.today()

результат робити функції - стрічка
f'User {login} created account on {date} with password "{password}". Additional information: {notes}'

задекоруйте написаним в завданні 1 декоратором
"""

##############################################################################
############                                                     #############
############                      TASK 3                         #############
############                                                     #############
##############################################################################
"""
створіть умову if name == main (тут ціленаправлено написано не вірно, як вірно - ви знаєте)
в цій умові створіть assert на всі створені функції (окрім декоратора), викликайте функції з різними параметрами 
(довжина слів, різні текстовки....)
на кожну функцію, що використовується в декораторі, має бути мінімум 3 ассерта,

функцію registration перевіряйте з огляду на роботу декоратора (ключі, значення). обовязково перевірте кількість ключів, 
тип даних в значеннях, назви ключів, значення отриманого результату в залежності від переданих даних   

ВАЖЛИВО 
функцію registration ассертимо ТІЛЬКИ при передачі їй валідних даних (поля паролю)
"""

##############################################################################
############                                                     #############
############                      TASK 4                         #############
############                     HAVE FUN                        #############
############                                                     #############
##############################################################################

import datetime


def is_valid_length(value, length=10):
    """
    Function for checking that strint is more than 10
    :param value: any type value, which can be converted to str
    :param length: value for comparation
    :return: False if less, True is more than 10
    """
    return False if len(str(value)) < length else True


def has_any_symbols(value):
    """
    Function which checks that string contains at least one symbol
    :param value: any type value, which can be converted to str
    :return: True if at least one symbol is present in the string
    """
    for i in str(value):
        if not i.isalpha():
            continue
        return True


def has_any_numbers(value):
    """
    Function for checking that string contains at least one number
    :param value: any type value, which can be converted to str
    :return: True if at least one number is present in the string
    """
    for i in str(value):
        if not i.isdigit():
            continue
        return True


def has_any_marks(value):
    """
    Function for checking that string contains at least one '!' symbol
    :param value: any type value, which can be converted to str
    :return: True if at least one number is present in the string
    """
    for i in str(value):
        if not i == '!':
            continue
        return True


def is_string(value):
    """
    Function for checking that value has type 'str'
    :param value: any value
    :return: True if value has type string
    """
    return False if not type(value) == str else True


def str_more_100(value, length=100):
    """
    Function for cutting string, if it is more than 100 symbols, and last symbols are '...' in the end
    :param value: str
    :param length: value for comparation
    :return: String with 100 symbolds and '...' in the end or string less than 100 symbols
    """
    return value[:97] + "..." if len(value) > length else value


def wrap_validate(func):
    """
    Decorator for checking that 'password' key is present in the function parameters, if no raise AttributeError
    If present - check that 'password' with such functions: is_valid_length, has_any_symbols, has_any_marks,
    is_string and str_more_100
    And str_more_100 cuts function result if it is more that 100 symbols
    :param func: function
    :return: dict with func result and info is password secure or no
    """
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
            return {'result': func_result,
                    'is_secure': True}
        return {'result': func_result,
                'is_secure': False}

    return check_password


@wrap_validate
def registration(id_user, login, notes, *, password):
    """
    Function which returns string with information which user and when created login and password
    :param id_user: int
    :param login: string
    :param notes: string
    :param password: string
    :return: String with the results
    """
    date = datetime.date.today()
    return f'User {login} created account on {date} with password "{password}". Additional information: {notes}'


if __name__ == '__main__':
    registration(56, 'user_name', 'hi', password=7897)
    registration(8439, 'Lola', 'she is new', password='')
    registration(8434, 'Kagura', 'she is new', dfsfd='')
    registration(839, 'Jason', 'this is very long notes', password='hhjkhjyijhkj23!')
    registration(458, 'Lola', 'she is new', password='hhjkhjyijhkj23!')
    registration(458, 'Lola', 678, password='hhjkhjyijhkj23!')
    registration('458', 'Lola', she is new, password='hhjkhjyijhkj23!')
    registration(password=45)
    registration(787)

    assert type(registration(458, 'Lola', 'she is new', password='hhjkhjyijhkj23!')) == dict, 'not dict'
    assert registration(458, 'Lola', 'she is new', password='67!').get('is_secure'), 'not secure'
    assert registration(458, 'Lola', 'she is new', password='6dfsty434sf7!').get('is_secure'), 'not secure'

    assert is_valid_length(''), 'not valid length'
    assert is_valid_length(10), 'not valid length'
    assert is_valid_length(1234567890), 'not valid length'

    assert has_any_symbols(678), "doesn't have symbols"
    assert has_any_symbols('!@#$%^&*()_+'), "doesn't have symbols"
    assert has_any_symbols('qwertyuiopasdfghjklzxcvbnm'), "doesn't have symbols"
    assert has_any_symbols('!6asdf'), "doesn't have symbols"

    assert has_any_numbers('fdsfs'), "doesn't have numbers"
    assert has_any_numbers('4672'), "doesn't have numbers"
    assert has_any_numbers('!@#$%6df3'), "doesn't have numbers"

    assert has_any_marks('fdsfs'), "doesn't have '!'"
    assert has_any_marks('fd!sfs'), "doesn't have '!'"
    assert has_any_marks('123df!@#$%^&*('), "doesn't have '!'"

    assert is_string(5454), 'not str'
    assert is_string('efsdxdfsd'), 'not str'
    assert is_string([]), 'not str'
    assert is_string(()), 'not str'

    # task 4
    print('Має бути один — і, бажано, тільки один — очевидний спосіб зробити це. Хоча спочатку він може бути й не очевидним, якщо ви не голландець.')
