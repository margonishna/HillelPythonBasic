# Abstract class

# class Vehicle:
#
#     def horn(self):
#         print('TUTUUUUU')
#
#     def run(self):
#         print('In run')
#         return self._run()
#
#     def _run(self):
#         raise NotImplementedError()
#
#
# class Car(Vehicle):
#     def _run(self):
#         print('Run in car')
#
#
# class Bus(Vehicle):
#     def _run(self):
#         print('Run in bus')
#
#
# bus1 = Bus()
#
# bus1.run()


# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#
#     @abstractmethod
#     def horn(self):
#         pass
#
#     @abstractmethod
#     def run(self):
#         pass
#
#
# class Car(Vehicle):
#     pass
#
#
# class Bus(Vehicle):
#
#     def horn(self):
#         print('Beeep!!')
#
#     def run(self):
#         print('In BUS run')
#
#
# bus1 = Bus()
#
# bus1.run()
# bus1.horn()


# class Example:
#
#     attr1 = 1
#
#     def foo(self):
#         pass
#
#
# e = Example()
#
# print(e.attr1)
# print(e.foo())


#  magic methods

# class Example:
#
#     attr1 = 1
#
#     def __new__(cls, *args, **kwargs):
#         print(f'in __new__ {args} {kwargs}')
#         instance = object.__new__(cls)
#
#         return instance
#
#     def __init__(self, val):
#         print(f'in __init__ val is {val}')
#         self.attr1 = val
#
#
# e = Example(2)


# class SingletOne:
#
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = object.__new__(cls)
#
#         return cls._instance
#
#     def __repr__(self):
#         return f'SingletOne object {id(self)}'
#
#
# single_object1 = SingletOne()
# print(id(single_object1))
#
# single_object2 = SingletOne()
# print(id(single_object2))
#
# print(single_object2)


# class Example:
#
#     attr1 = 1
#
#     def __str__(self):
#         return f'SingletOne object {id(self)}'
#
#     def __int__(self):
#         return self.attr1 * 10
#
#     def __float__(self):
#         return self.attr1 * 10.1
#
#     def __bool__(self):
#         return bool(self.attr1)
#
#
# e = Example()
#
# res = str(e)
# print(res)
#
# res = int(e)
# print(res)
#
# res = float(e)
# print(res)
#
# res = bool(e)
# print(res)

#
# class Example:
#
#     attr1 = 1
#
#     def __eq__(self, other):  # ==
#         if not isinstance(other, self.__class__):
#             raise TypeError
#
#         return True
#
#     def __lt__(self, other):  # <
#         if not isinstance(other, self.__class__):
#             raise TypeError
#
#         return True
#
#     def __le__(self, other):  # <=
#         if not isinstance(other, self.__class__):
#             raise TypeError
#
#         return True
#
#     def __gt__(self, other):  # >
#         if not isinstance(other, self.__class__):
#             raise TypeError
#
#         return True
#
#     def __ge__(self, other):  # >
#         if not isinstance(other, self.__class__):
#             raise TypeError
#
#         return True
#
#
# ex1 = Example()
# # ex2 = Example()
# ex2 = ex1
#
# res = ex1 == ex2
#
# print(res)


# class Example:
#
#     attr1 = 1
#
#     def __add__(self, other):  # +
#
#         self.attr1 += other.attr1
#         return self
#
#     def __sub__(self, other):  # -
#
#         return self
#
#     def __mul__(self, other):  # *
#
#         return self
#
#     def __truediv__(self, other):  # /
#
#         return self
#
#
# ex1 = Example()
# ex2 = Example()
#
# res = ex1 + ex2
#
# print(res)
# print(res.attr1)


# class Example:
#     attr1 = 1
#
#     def __len__(self):
#         return self.attr1
#
#     def __contains__(self, item):
#         return True
#
#
# e = Example()
#
# # print(len(e))
#
# print('abcd' in e)
#
#
# class Example:
#     attr1 = 1
#
#     def __init__(self, val):
#         print(self.attr1)
#         self.attr1 = val
#
#     def __getattribute__(self, item):
#         print(f'__getattribute__ {item}')
#         return super().__getattribute__(item)
#
#     def __getattr__(self, item):
#         print(f'__getattr__ {item}')
#         return
#
#     def __setattr__(self, key, value):
#         print('__setattr__', key, value)
#         super().__setattr__(key, value)
#
#
# e = Example(12345)
#
# print(e.attr1234)
#
#
# class Example:
#     attr1 = 1
#
#     def __init__(self, val):
#         self.attr1 = val
#
#     def __getitem__(self, item):
#         print(f'__getitem__ {item}')
#         return getattr(self, item, None)
#
#     def __setitem__(self, key, item):
#         print(f'__getitem__ {item}')
#         return setattr(self, key, item)
#
#
# e = Example(124)
#
# print(e['attr1'])
# print(e['attr1qwer'])
# e['attr1qwer'] = 123
#

#
# class Point:
#
#     _x = None
#     _y = None
#
#     @property  # getter
#     def x(self):
#         return self._x
#
#     @x.setter
#     def x(self, value):
#         if not isinstance(value, int):
#             raise TypeError
#         self._x = value
#
#     @property  # getter
#     def y(self):
#         return self._y
#
#     @y.setter
#     def y(self, value):
#         if not isinstance(value, int):
#             raise TypeError
#         self._y = value
#
#     def __init__(self, x_coord, y_coord):
#         self.x = x_coord
#         self.y = y_coord
#
#     def __add__(self, other):
#         return Line(self, other)
#
#
# class Line:
#     """
#     """
#     begin = None
#     end = None
#
#     def __init__(self, begin_point: Point, end_point: Point):
#         self.begin = begin_point
#         self.end = end_point
#
#     @ property
#     def length(self):
#         print('in length_getter')
#         return ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5
#
#     def __eq__(self, other):
#         return self.length == other.length
#
#
# point1 = Point(0, 3)
# point1.x = 100
# point2 = Point(4, 0)
#
#
# line1 = point1 + point2
#
# print(type(line1))
# print(line1.length)
#
# line2 = point1 + point2
#
# print(line1 == line2)
#
#
# def res_to_dict(func):
#     """
#     Result of function to dict
#     Args:
#         func:
#     Returns:
#     """
#     def wrapper(*args, **kwargs):
#         # check kwargs
#         res = func(*args, **kwargs)
#
#         # res `str` -> res `dict`
#         return res
#
#     return wrapper
#
#
# @res_to_dict
# def foo(*args, **kwargs):
#     """
#     Args:
#         *args:
#         **kwargs:
#     Returns:
#         (str):
#     """
#     return


# def class_decorator(cls):
#
#     def wrapper(*args, **kwargs):
#         print(cls)
#         return cls
#
#     return wrapper
#
#
# @class_decorator
# class Example:
#     attr = 1
#
#
# ex = Example()
#
# print(Example)


assert 0  # False -> Assertion Error
# assert 1  # False -> Assertion Error


# import pytest

