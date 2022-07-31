# from library import foo
#
# foo()

# import random
#
# print(random.randint(1, 100))

# import requests

# from random import randint
#
# print(randint(1, 100))


# import random as R
#
# print(R.randint(100, 200))

# from random import randint as RandInt
#
# print(RandInt(1, 100))


# from random import randint, choice
#
# print(randint(1, 100))
# print(choice('abcdef'))

#
# from random import *  # all names # BAD IDEA!!!!!
#
#
# print(choice('abcdef'))


# import library
#
# library.foo()
# print(library.variable1)
# print(library.variable2)


# from library import foo as FOO

# FOO()


# import library   # python3 library.py

# library.foo()

# print(f'__name__ in example is {__name__}')

# lambda


# colors = ["Red", "Grey", "Blue", "Green", "Orange", "Yellow"]
#
#
# # def foo(val):
# #     return val[-1]
#
#
# print(sorted(colors))
# # print(sorted(colors, key=foo))
#
# print(sorted(colors, key=lambda val: val[-1]))


# lambda x: x[-1]

# lambda x, y: x + y


# BAD IDEA
# add = lambda x, y: x + y
#
#
# print(add(1, 3))
#
#
# lst = ['13', '2', '33', '4']
#
#
# def foo(val):
#     return float(val)
#
#
# # BAD IDEA!!
# print(sorted(lst, key=lambda val: float(val)))
#
# print(sorted(lst, key=float))
#
#
# print(sorted(lst, key=lambda val: float(val) + 2))


# useful functions

# data transformations
#
# res = str(1234)
# res = int('1234')
# res = bool(None)
#
# # math functions
#
# res = max(1, 3, 42, 0, 2)
# print(res)
#
#
# res = min(1, 3, 42, 0, 2)
# print(res)
#
# res = max([1, 333, 82, 83, 0, 2], key=lambda val: val if val % 2 == 0 else 0)
# print(res)
#
#
# res = sum([1, 333, 82, 83, 0, 2])
# print(res)
#
#
# # range
#
# rng = range(3, 10, 2)
#
# for i in rng:
#     print(i)


# # enumerate
#
# for i in enumerate('bla bla bla'):
#     print(i)
#
# print(dict(enumerate('bla bla bla')))


# map

def foo(val):
    return val % 2


data = (3, 4, 5, 6)

for i in data:
    res = foo(i)
    print(res)


mapped = map(foo, data)  # i from data, i = foo(i)

for i in mapped:
    print(i)



