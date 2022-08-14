# OOP

# Abstraction
# Encapsulation
# Inheritance
# Polymorphism
#
#
# class A:
#     def foo(self):
#         print('Foo in class A')
#
#
# class B:
#     def foo(self):
#         print('Foo in class B')
#
#
# class C(B):
#     def foo(self):
#         print('Foo in class C')
#
#
# class D(C, A):
#     def foo(self):
#         print('Foo in class D')
#
#
# """
#   D
# |   |
# A   C
#     |
#     B
# """
#
# # print(D.mro())
#
# obj = D()
#
# obj.foo()

#
# class Human:
#     name = 'Bill'
#     age = 30
#
#     def __init__(self, age, name, *args, **kwargs):
#         self.age = age
#         self.name = name
#
#
# class AddressMixin:
#     city = ''
#     street = ''
#     building = ''
#
#
# class User(Human, AddressMixin):
#     login = ''
#     password = ''
#     avatar = ''
#
#     def __init__(self, age, name, login, password, avatar, *args, **kwargs):
#         # super().__init__(age, name)
#         self.age = age
#         self.name = name
#         self.login = login
#         self.password = password
#         self.avatar = avatar
#
#         # Human.__init__(self)
#
#
# class Office(AddressMixin):
#     pass


# classmethod
# staticmethod

#
# class Example:
#
#     arrt = 0
#
#     def __init__(self, attr):
#         self.arrt = attr
#
#     def foo(self):
#         print(f'attr is {self.arrt}')
#
#     @classmethod
#     def bar(cls):
#         print(f'attr is {cls.arrt}')
#
#     @staticmethod
#     def spam(arg1, arg2):
#         print(f'attr is unknown')
#         print(f'args {arg1} {arg2}')
#
#     def eggs(self):
#         print(f'self attr is {self.arrt}')
#
#         print(f'cls attr is {self.__class__.arrt}')
#
#
# e = Example(100500)
#
# print(e.arrt)
# e.foo()
#
# print(Example.arrt)
# e.bar()
#
# e.spam(1, 2)
# e.eggs()
# print(e.__class__.arrt)
#
# a = 10
#
#
# class MyInt(a.__class__):
#     pass
#
#
# my_int = MyInt(100)
#
# print(type(my_int))
# print(my_int)

#
# class Example:
#     attr1 = None
#     attr2 = None
#
#     def __init__(self, attr1):
#         self.attr1 = attr1  # <- __dict__['attr1'] = attr1
#
#
# e = Example(100)
#
# print(e.attr1)
# print(e.attr2)
#
# Example.attr2 = 500
#
# print(e.attr1)
# print(e.attr2)
#
#
# print(Example.__dict__)
# print(e.__dict__)


# import turtle

# class Point:
#     x = 0
#     y = 0
#     name = None
#
#     def __init__(self, x_coord, y_coord, name=None):
#         if not isinstance(x_coord, int) or not isinstance(y_coord, int):
#             raise TypeError
#         self.x = x_coord
#         self.y = y_coord
#         if name is not None:
#             self.name = name
#
#
# point1 = Point(0, 3)
# point2 = Point(4, 0)
#
# # class Line:
# #     # association - composition
# #     begin = None
# #     end = None
# #
# #     def __init__(self, begin_x, end_x, begin_y, end_y):
# #         self.begin = Point(begin_x, end_x)
# #         self.end = Point(begin_y, end_y)
# #
# #     def get_length(self):
# #         return 0
#
#
# class Line:
#     # association - aggregation
#     begin = None
#     end = None
#
#     def __init__(self, begin_point: Point, end_point: Point):
#         self.begin = begin_point
#         self.end = end_point
#
#     def get_length(self):
#
#         return ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5
#
#
# line1 = Line(point1, point2)
#
# print(line1.get_length())
#
#
# line1.end = Point(0, 0)
#
# print(line1.get_length())

#
# class Point:
#     _x = None
#     _y = None
#
#     def x_getter(self):
#         return self._x
#
#     def x_setter(self, value):
#         if not isinstance(value, int):
#             raise TypeError
#         self._x = value
#
#     def y_getter(self):
#         return self._y
#
#     def y_setter(self, value):
#         if not isinstance(value, int):
#             raise TypeError
#         self._y = value
#
#     y = property(y_getter, y_setter)
#     x = property(x_getter, x_setter)
#
#     def __init__(self, x_coord, y_coord):
#         self.x = x_coord
#         self.y = y_coord
#
#
# point1 = Point(0, 3)
# point1.x = 100
# point2 = Point(4, 0)
#
#
# class Line:
#     # association - aggregation
#     begin = None
#     end = None
#
#     def __init__(self, begin_point: Point, end_point: Point):
#         self.begin = begin_point
#         self.end = end_point
#
#     def length_getter(self):
#         print('in length_getter')
#         return ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5
#
#     def length_setter(self, val):
#         print(f'in length_setter {val}')
#
#     length = property(length_getter, length_setter)
#
#
# line1 = Line(point1, point2)
#
#
# # print(line1.length)
# # print(line1.length_getter())
# #
# # print(type(line1.length))
# #
# # line1.length = 100
# line1.length = line1.length


# class Point:
#     _x = None
#     _y = None
#
#     x = property()
#
#     @x.getter
#     def x(self):
#         return self._x
#
#     @x.setter
#     def x(self, value):
#         if not isinstance(value, int):
#             raise TypeError
#         self._x = value
#
#     y = property()
#
#     @y.getter
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
#
# point1 = Point(0, 3)
# point1.x = 100
# point2 = Point(4, 0)


class Point:
    _x = None
    _y = None

    @property  # getter
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._x = value

    @property  # getter
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._y = value

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord


point1 = Point(0, 3)
point1.x = 100
point2 = Point(4, 0)


class Line:

    begin = None
    end = None

    def __init__(self, begin_point: Point, end_point: Point):
        self.begin = begin_point
        self.end = end_point

    @ property
    def length(self):
        print('in length_getter')
        return ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5


line1 = Line(point2, point1)

print(line1.length)

