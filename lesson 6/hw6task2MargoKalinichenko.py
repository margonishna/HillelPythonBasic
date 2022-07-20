"""
Task 2
Напишіть функцію, що приймає два аргументи. Функція повинна
якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
у будь-якому іншому випадку повернути кортеж з цих аргументів
"""

value1 = input("Введіть одне значення:")
value2 = input("Введіть одне значення:")


def turned_float(arg1):
    try:
        changed_value = float(arg1)
    except ValueError:
        return arg1
    else:
        return changed_value


result1 = turned_float(value1)
result2 = turned_float(value2)


def two_values(arg1, arg2):
    if type(arg1) == float and type(arg2) == float:
        multiply = arg1 * arg2
        return multiply
    elif type(arg1) == str and type(arg2) == str:
        str_all = arg1 + arg2
        return str_all
    elif type(arg1) == str and type(arg2) == float:
        dict1 = {}
        dict1[arg1] = arg2
        return dict1
    else:
        tuple1 = (arg1, arg2)
        return tuple1


result3 = two_values(result1, result2)
print(f'Результат: {result3}')
