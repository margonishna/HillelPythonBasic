import random


WIN_RULES = {
    'rock': ['scissors', 'lizard', 'bug'],
    'scissors': ['paper'],
    'paper': ['rock'],
    'lizard': [],
    'bug': [],

}


def comp_choice():
    """

    Returns:
        comp_choice (str)
    """
    # choise = random.choice(list(WIN_RULES))
    choise = random.choice(['rock', "g", 5])
    return choise


def game():
    comp = comp_choice()
    user = 'paper'

    if comp == user:
        d = 'Draw'
    elif user in WIN_RULES[comp]:
        d = 'Comp won'
    else:
        d = 'User won'

    return d


import functools


def money_formating(round_precision: int = 2):
    def money_formating(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            func_type = type(result)
            if func_type == str:
                return result

            return float(result).__round__(round_precision)

        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__
        return wrapper
    return money_formating


@money_formating(10)
def get_rectangle_data(side1: int, /, side2: int, *, is_perimeter: bool = True) -> int:
    """mmmmmmmm"""
    rules = {
        True: lambda: (side1 + side2) * 2,
        False: lambda: side1 * side2,
        'square': lambda: side1 * side2,
    }

    result = rules[is_perimeter]()

    #
    # try:
    #     n = result/random.randint(0, 5)
    # except ValueError as er:
    #     return er
    # else:
    #     return n
    # finally:
    #     return result # here!!!!!!!!!!!

    return result


if __name__ == '__main__':
    # get_rectangle_data(2, 6, is_perimeter=True)
    # assert comp_choice()
    # assert comp_choice() in WIN_RULES, 'NOOOOOOO'
    # assert type(comp_choice()) == str, 'not a str'
    # assert type(WIN_RULES) == dict, 'not a dict'

    # assert get_rectangle_data(1, 1, is_perimeter=True) == 4, 'wrong perimeter'
    # assert get_rectangle_data(1, 1, is_perimeter=False) == 1, 'wrong square'
    # assert type(get_rectangle_data(1, 1, is_perimeter=False)) == int, 'wrong square'
    pass

if __name__ == '__main__':
    print(get_rectangle_data)
    print(get_rectangle_data.__name__)
    print(get_rectangle_data.__doc__)

    print(get_rectangle_data(1.56565555555001, 1, is_perimeter=True))


# func_list = {
#     get_rectangle_data,
#     comp_choice,
# }
#
#
# user = input('>>>>>>>>')
#
# for func in func_list:
#     if func.__name__ == 'get_rectangle_data':
#         print(func(1.56565, 1, is_perimeter=True))
