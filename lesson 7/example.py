# def foo(arg1, arg2=0):
#
#     return arg1 + arg2
#
#
# res = foo(1, 2)
#
# print(res)
#
#
# def foo(*args):  # *args - positional
#     print(type(args))
#     print(args)
#     return
#
#
# res = foo()
# res = foo(1, 2)
# res = foo(1, 2, 13, 3, 4, 5, 6, 3, 4, 5, 6, 5)

# my_args = [1, 2, 3, 4, 5, 6, 7, 8]
#
#
# def foo(arg_list):  # *args - positional
#     print(type(arg_list))
#     print(arg_list)
#     return
#
# res = foo(my_args)

#
# def foo(*args):  # *args - positional
#     print(type(args))
#     print(args)
#     return args
#
#
# my_args = [1, 2, 3, 4, 5, 6, 7, 8]
#
#
# res = foo(*my_args)  # res = foo(1, 2, 3, 4, 5, 6, 7, 8)
# print(res)
#
#
# res = foo('1', '3', '4', *my_args)  # res = foo('1', '3', '4', 1, 2, 3, 4, 5, 6, 7, 8)
# print(res)
#
# res = foo(*my_args, '1', '3', '4')  # res = foo(1, 2, 3, 4, 5, 6, 7, 8, '1', '3', '4')
# print(res)

# my_args = [1, 2, 3, 4, 5, 6, 7, 8]
#
#
# def foo(arg1, arg2, *args):  # *args - positional
#     print('arg1, arg2', arg1, arg2)
#     print('args', args)
#     return 0
#
#
# res = foo('1', '3')
# res = foo('1', '3', 1, 3, 3)
# res = foo('1', '3', *my_args)
# res = foo(*my_args)

#
# def foo(**kwargs):  # **kwargs - named
#
#     print('kwargs', kwargs)
#     print(type(kwargs))
#     return 0
#
#
# res = foo()
# res = foo(a=10)
# res = foo(a=10, b=[], c={}, d=123)

#
# def foo(a, b=20, **kwargs):  # **kwargs - named
#     print(a)
#     print(b)
#     print('kwargs', kwargs)
#     print(type(kwargs))
#     return 0
#
#
# res = foo(10, 12)
# res = foo(10)
# res = foo(a=10, b=20, c=30, d=40)
#
# data_dict = {
#     'a': 10,
#     'b': 120,
#     'd': 120,
# }
#
#
# def foo(a, b=20, **kwargs):
#     print(a)
#     print(b)
#     return 0
#
#
# res = foo(**data_dict)  # foo(a=10, b=120)

# def foo(a, b, c=10, d=20, *args, **kwargs):
#     print(f'{a} {b} {c} {d}')
#     print(f'{args}')
#     print(f'{kwargs}')
#     return 0
#
#
# data_dict = {
#     'c': 10,
#     'd': 20,
#     'm': 30,
#     'n': 40,
# }
#
# data_list = [1, 2]
#
# res = foo(1, 2, 3, 4, 5, 6)
# res = foo(1, 2, 3, 4, 5, 6, m=40, k=80)
# res = foo(1, 2, m=40, k=80)
# res = foo(*data_list, **data_dict)

# docstrings

# def foo(a, b):
#     """Function for bla bla bla"""
#     print(f'{a} {b}')
#     return 0

# from typing import Union
#
# # type annotation
#
#
# def foo(a: Union[int, float], b: float = 10) -> str:
#     """Function for bla bla bla"""
#
#     print(f'{a} {b}')
#     return
#
#
# res = foo('dvb', [2, 3])
#
#
# def foo(a, b=10):
#     """
#     Function for bla bla bla reStructuredText
#
#     :param a: description for argument a
#     :type a: int|float|str
#     :param b:
#     :return:
#     :rtype: tuple
#     """
#     print(f'{a} {b}')
#     return
#
#
# foo('1', 1)
#
#
# def foo(a, b=10):
#     """
#     Function for bla bla bla
#     Args:
#         a (int|float):  description for argument a
#         b:
#     Returns:
#         (tuple):
#     """
#     print(f'{a} {b}')
#     return


# recursion


# f = !5

# f = 5 * 4 * 3 * 2 * 1

# f = 5 * f(4)


# f = n * n-1 * n-2 ..... n-k * 1

# f - > n * f(n-1)
#
#
# counter = 0
#
#
# def factorial_recursive(n):
#     global counter
#     counter += 1
#     if n == 1:
#         return 1
#
#     return n * factorial_recursive(n-1)
#
#
# res = factorial_recursive(5)
# print(res)
#
# print(counter)
#
# counter = 0

# 1 1 2 3 5 8 13 21 43 55 89 ....

# f[n] = f[n-1] + f[n-2]

#
# counter = 0
#
#
# def fib_rec(n):
#
#     global counter
#     counter += 1
#
#     if n in (1, 2):
#         return 1
#
#     return fib_rec(n-1) + fib_rec(n-2)
#
#
# print(fib_rec(30))
# print(counter)

# O(n)

# O(1)

# O(logn)

# O(n)

# O(n**k)

# O(k**n)


# counter = 0
#
#
# def fib_plain(n):
#
#     global counter
#     counter += 1
#
#     fib1 = fib2 = 1
#
#     if n in (1, 2):
#         return fib1
#
#     for i in range(n - 2):
#         fib1, fib2 = fib2, fib1 + fib2
#
#     return fib2
#
#
# print(fib_plain(100))
# print(counter)


data_dict = {
    'a': 1,
    'b': 1,
    'c': {
        'a': 2,
        'b': {
            'a': 3,
            'b': {
                'a': 4,
            }
        },
        'c': 2
    }
}


# for k, v in data_dict.items():
#     if not isinstance(v, dict):
#         print(k, v)
#     else:
#         for k2, v2 in v.items():
#             if not isinstance(v2, dict):
#                 print(k2, v2)


def data_from_dict_rec(data):

    for key, value in data.items():
        if not isinstance(value, dict):  # type(value) == dict
            print(key, value)
        else:
            data_from_dict_rec(value)


data_from_dict_rec(data_dict)


# type(value) == int or type(value) == float
# isinstance(value, (int, float))


