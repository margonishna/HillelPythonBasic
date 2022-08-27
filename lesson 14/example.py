# # Iterator
#
# my_str = '123456789'
#
# my_str_iter = iter(my_str)
#
# print(type(my_str_iter))
#
# print(next(my_str_iter))
# print(next(my_str_iter))
# print(next(my_str_iter))
# print(next(my_str_iter))
# print(next(my_str_iter))
# print(next(my_str_iter))
#
#
# for i in '123456789':  # my_str_iter = iter('123456789')
#     # try:
#     #     i = next(my_str_iter)
#     # except StopIteration:
#     #     break
#     print(i)
#
#
# class Example:
#     pass
#
#
# e = Example()
#
# e_iter = iter(e)


# class Counter:
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return 1
#
#
# c = Counter()


# class Counter:
#     limit = 0
#     current_position = 0
#
#     def __init__(self, limit):
#         self.limit = limit
#
#     def __iter__(self):
#         self.current_position = 0
#         return self
#
#     def __next__(self):
#         if self.current_position >= self.limit:
#             raise StopIteration
#
#         self.current_position += 1
#
#         return self.current_position
#
#
# c = Counter(5)
#
#
# for i in c:
#     print(i)
#
# print('--->',  c.current_position)
#
# for i in c:  # iter(c)
#     print(i)

#
# class Point:
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
#
# point1 = Point(0, 3)
# point2 = Point(4, 0)
#
#
# class Line:
#
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
#     # def __iter__(self):
#     #     self.points = (self.begin, self.end)
#     #     self.idx = -1
#     #     return self
#
#     # def __next__(self):
#     #     self.idx += 1
#     #
#     #     if self.idx >= len(self.points):
#     #         raise StopIteration
#     #
#     #     return self.points[self.idx]
#
#     # def __next__(self):
#     #     self.idx += 1
#     #
#     #     if self.idx == 0:
#     #         return self.begin
#     #     elif self.idx == 1:
#     #         return self.end
#     #     else:
#     #         raise StopIteration
#
#     def __iter__(self):
#         self.iter = iter((self.begin, self.end))
#         return self.iter
#
#     def __next__(self):
#         return next(self.iter)
#
#
# line1 = Line(point2, point1)
#
# print(line1.length)
#
# for point in line1:
#     print(point)


# def my_generator():
#     # return 1
#
#     print('before')
#     yield 1
#     print('after')
#
#     yield 2
#
#
# print('-------')
# res = my_generator()
# print('-------')
#
# print(type(res))
#
# for i in res:
#     print('-->')
#     print(i)

#
# def counter(limit):
#     print('Start generator')
#
#     value = 0
#     while True:
#         print('Before yield')
#         yield value
#         print('After yield')
#
#         if value >= limit:
#             return
#
#         value += 1
#
#
# for i in counter(5):
#     print(i)


# context manager


# with open('ex.txt', 'w') as file:
#     print(file)
#
#
# class Example:
#
#     def __enter__(self):
#         print('In enter')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f'In exit {exc_type} {exc_val} {exc_tb}')
#         return True
#
#
# with Example():
#     print('Inside manager')
#     1/0
#     print('Inside manager after zero division')

# import time
#
#
# class Example:
#     start = None
#
#     def __enter__(self):
#         self.start = time.time()
#         print('In enter')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f'In exit {exc_type} {exc_val} {exc_tb}')
#         print('Time spent: ', time.time() - self.start)
#         return True
#
#
# ex = Example()
#
# with ex as obj:
#     print(obj)
#     x = [a**a for a in range(1000)]
#     time.sleep(2)


# # descriptor
#
# class OnlyStrDescriptor:
#
#     def __set__(self, instance, value):
#         """
#         Args:
#             instance: object of Example class
#             value: value
#         """
#         print('__set__', value)
#         if not isinstance(value, str):
#             raise TypeError
#
#         instance._value = value
#
#     def __get__(self, instance, owner):
#         """
#         Args:
#             instance: object of Example class
#             owner: Example class
#         """
#         print('__get__')
#         return instance._value
#
#
# class Example:
#
#     some_attr = OnlyStrDescriptor()
#
#
# e = Example()
#
# e.some_attr = 'qwert'
# e.some_attr = 1111
# print(e.some_attr)

#
# class Example:
#     val1 = 2
#     val2 = 4
#
#     def val_sum_getter(self):
#         return self.val1 + self.val2
#
#     def val_sum_setter(self, val):
#         print('val_sum_setter', val)
#
#     val_sum = property(val_sum_getter, val_sum_setter)
#
#
# e = Example()
#
# print(e.val_sum)
#
# e.val_sum = 100

#
# class Example:
#     val1 = 2
#     val2 = 4
#
#     @property  # val_sum = property(val_sum)
#     def val_sum(self):
#         return self.val1 + self.val2
#
#     @val_sum.setter
#     def val_sum(self, val):
#         print('val_sum_setter', val)
#
#
# e = Example()
#
# e.val_sum = 1


word = 'asdfghj'


def get_count(raw_str):
    letters = 'aeiou'
    counter = 0

    # for char in letters.lower():
    #     counter += raw_str.lower().count(char)

    for char in raw_str.lower():
        if char in letters:
            counter += 1

    return counter


print(get_count('abIcedae'))

