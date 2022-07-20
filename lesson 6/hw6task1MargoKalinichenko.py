"""
Task 1
Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
Якщо перетворити не вдається функція має повернути 0.
"""

value1 = input("Введіть одне значення:")


def turned_float(arg1):
    try:
        changed_value = float(arg1)
    except ValueError:
        return 0
    else:
        # print(changed_value)
        return changed_value


result = turned_float(value1)

if type(result) != float:
    print(f'Неможливо перетворити на float, результат: {result}')
elif type(result) == float:
    print(f'Перетворено на float: {result}')
