#
# def foo():
#
#     return 1, '1'
#
#
# res = foo()
#
# first = res[0]
# second = res[1]
#
# first, second = foo()


# zip
#
# lst1 = [1,   2,    3,   4,  5]
# lst2 = ['a', 'b', 'c']
# lst3 = [[],  {},  None, True]
#
# #
# # for i in range(min(len(lst1), len(lst2), len(lst3))):
# #     print(lst1[i], lst2[i], lst3[i])
#
#
# zipped = zip(lst1, lst2, lst3, range(50, 100, 4))
#
# for i in zipped:
#     print(i)
#
#
# # reversed
#
# data = '1234567890'
#
# rev = reversed(data)
#
# print(rev)
#
# for i in rev:
#     print(i)

# sorted

# res = sorted([1, 3, 2, 4, 5, 6, 11, 7, 0, -2])
#
# print(res)
#
# res = sorted((1, 3, 2, 4, 5, 6, 11, 7, 0, -2))
#
# print(res)
#
# res = sorted((1, 3, 2, 4, 5, 6, 11, 7, 0, -2), reverse=True)
# print(res)
#
# res = sorted((1, 3, 2, 4, 5, 6, 11, 7, 0, -2), reverse=True, key=lambda x: x % 3)
# print(res)
#
#
# # filter
#
# filtered = filter(lambda x: x % 2 == 0, (1, 3, 2, 4, 5, 6, 11, 7, 0, -2))
#
# # print(type(filtered))
#
# for i in filtered:
#     print(i)
#
#
# a = 10
# b = 20
#
# if a > 0 and b > 0 and a > b and a + b % 2 == 0:
#     print('Match')
#
#
# conditions = (
#     a > 0,
#     b > 0,
#     a > b,
#     a + b % 2 == 0,
# )
#
#
# if all(conditions):  # a > 0 and b > 0 and a > b and a + b % 2 == 0
#     print('Match')
#
# # OR
#
# if a > 0 or b > 0 or a > b or a + b % 2 == 0:
#     print('Match')
#
# conditions = (
#     a > 0,
#     b > 0,
#     a > b,
#     a + b % 2 == 0,
# )
#
# if any(conditions):  # a > 0 or b > 0 or a > b or a + b % 2 == 0
#     print('Match')


# open

"""
r  - read
w  - create / rewrite
x
a  - append

b - binary
t - text

+

"""

# file = open('example.txt', 'w')
#
# file.write('!!!')
#
# file.close()


# file = open('example.txt')   # 'rt'
#
# for line in file:
#     print(line)
#
# file.close()


# file = open('example.txt', 'a')
#
# file.write('!!!')
#
# file.close()


# file = open('example.txt', 'a')
#
# file.write('!!!')
#
# file.close()


# with open('example.txt', 'r') as file:  # file = open('example.txt', 'r')
#     for line in file:
#         print(line)


# DECORATOR

# print(id(1))
#
#
# def foo():
#     pass
#
#
# print(id(foo))

# -5 ... 255
# True, False, None

# val_1 = []
#
#
# def bar(arg_1):
#     print(id(arg_1))
#     return arg_1
#
#
# print(id(val_1))
#
# res = bar(val_1)
#
# print(id(res))


# def bar():
#
#     def inner_function():
#         return 'inner_function'
#
#     return inner_function
#
#
# res = bar()
#
# print(type(res))
# print(id(res))


# def function_to_decorate(*args, **kwargs):
#     print(f'I\'m just functon with args {args} and kwargs {kwargs}')
#
#
# def decorator(func):
#
#     def wrapper(*args, **kwargs):
#         print('Some actions before')
#         result = func(*args, **kwargs)
#         print('Some actions after')
#         return result
#
#     return wrapper
#
#
# # decorated_func = decorator(function_to_decorate)
# #
# # res = decorated_func(123, a=10, b=20)
#
# print('--------')
#
# res = function_to_decorate(123, a=10, b=20)
#
# print('--------')
#
# function_to_decorate = decorator(function_to_decorate)
#
# res = function_to_decorate(123, a=10, b=20)

#
# def decorator(func):
#
#     def wrapper(*args, **kwargs):
#         print('Some actions before')
#         result = func(*args, **kwargs)
#         print('Some actions after')
#         return result
#
#     return wrapper
#
#
# @decorator  # function_to_decorate = decorator(function_to_decorate)
# def function_to_decorate(*args, **kwargs):
#     print(f'I\'m just functon with args {args} and kwargs {kwargs}')
#
#
# @decorator
# def foo(*args, **kwargs):
#     print('I\'m foo')
#
#
# function_to_decorate(1, b=0)
# foo(1, b=0)


# def only_int_args_kwargs(func):
#
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             if not isinstance(arg, int):
#                 raise TypeError
#         for val in kwargs.values():
#             if not isinstance(val, int):
#                 raise TypeError
#
#         result = func(*args, **kwargs)
#         return result
#
#     return wrapper
#
#
# @only_int_args_kwargs
# def foo(arg1, arg2):
#     return arg1, arg2
#
#
# res = foo('1', 2)


# def check_types_args_kwargs(*data_types):
#
#     def outer_wrapper(func):
#
#         def inner_wrapper(*args, **kwargs):
#             for arg in args:
#                 if not isinstance(arg, data_types):
#                     raise TypeError
#             for val in kwargs.values():
#                 if not isinstance(val, data_types):
#                     raise TypeError
#
#             result = func(*args, **kwargs)
#             return result
#
#         return inner_wrapper
#
#     return outer_wrapper
#
#
# @check_types_args_kwargs(int, float)  # foo = check_types_args_kwargs(int, float)(foo)
# def foo(arg1, arg2):
#     return arg1, arg2
#
#
# # foo = check_types_args_kwargs(int, float)(foo)
#
# foo(1, 2.3)
# # foo('1', 2.3)
#
#
# @check_types_args_kwargs(str)  # foo = check_types_args_kwargs(int, float)(foo)
# def bar(arg1, arg2):
#     return arg1, arg2
#
#
# bar('1', '2')
# bar('1', None)


# def decorator1(func):
#
#     def wrapper(*args, **kwargs):
#         print('Some actions before  1')
#         result = func(*args, **kwargs)
#         print('Some actions after   1')
#         return result
#
#     return wrapper
#
#
# def decorator2(func):
#
#     def wrapper(*args, **kwargs):
#         print('Some actions before  2')
#         result = func(*args, **kwargs)
#         print('Some actions after   2')
#         return result
#
#     return wrapper
#
#
# @decorator2  # foo = decorator1(decorator2(foo))
# @decorator1
# def foo(*args, **kwargs):
#     print('Foo')
#
#
# foo(1, 2)


# GAME Guess number

# def game
    # get random number - into function

    # loop
        # get number from user - into function

        # if user guess - break  - into function
        # if not - continue


from random import randint


def get_random_number():
    """
    Returns:
        (int)
    """
    number = randint(1, 101)
    return number


def get_number_from_user():
    """
    Returns:
        (int)
    """
    while True:
        try:
            return int(input('Enter int: '))
        except:
            print('It\'s not int')


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


def game():
    number_to_guess = get_random_number()

    while True:
        user_number = get_number_from_user()
        if check_numbers(number_to_guess, user_number):
            break

    print('You WIN!!!!')


game()
