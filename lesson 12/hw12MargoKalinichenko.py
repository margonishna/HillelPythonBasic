"""
Доопрацюйте класс Line так,
щоб в атрибути begin та end обʼєктів цього класу можна було записати
тільки обʼєкти класу Point. Використовуйте property
Створіть класс Triangle (трикутник), який задається трьома точками
(обʼєкти классу Point). Реалізуйте перевірку даних, аналогічно до класу Line.
Визначет атрибут, що містить площу трикутника (за допомогою property).
Для обчислень можна використати формулу Герона (https://en.wikipedia.org/wiki/Heron%27s_formula)
"""


class Point:
    """
    Class, which describes coordinates of points. x is first coordinate, y is second coordinate.
    x and y can be gotten and set via property, only int objects can be set.
    """
    _x = None
    _y = None

    def x_getter(self):
        return self._x

    def x_setter(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._x = value

    def y_getter(self):
        return self._y

    def y_setter(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._y = value

    x = property(x_getter, x_setter)
    y = property(y_getter, y_setter)

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord


class Line:
    """
    Class Line has 'begin' and 'end' points.
    'begin' and 'end' can be gotten and set via property, only Point objects can be set.
    'length' is method, which counts length of the line between two points. Can be gotten via property.
    """
    _begin = None
    _end = None

    def begin_getter(self):
        return self._begin

    def begin_setter(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._begin = value

    def end_getter(self):
        return self._end

    def end_setter(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._end = value

    begin = property(begin_getter, begin_setter)
    end = property(end_getter, end_setter)

    def __init__(self, begin_point, end_point):
        self.begin = begin_point
        self.end = end_point

    def length_getter(self):
        length_value = ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5
        return length_value

    length = property(length_getter)


class Triangle:
    """
    Class Triangle has 'first', 'second' and 'third' points.
    'first', 'second' and 'third' can be gotten and set via property, only Point objects can be set.
    'square' is method, which counts square of the triangle between three points. Can be gotten via property.
    """
    _first = None
    _second = None
    _third = None

    def first_getter(self):
        return self._first

    def first_setter(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._first = value

    def second_getter(self):
        return self._second

    def second_setter(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._second = value

    def third_getter(self):
        return self._third

    def third_setter(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._third = value

    first = property(first_getter, first_setter)
    second = property(second_getter, second_setter)
    third = property(third_getter, third_setter)

    def __init__(self, first_point, second_point, third_point):
        self.first = first_point
        self.second = second_point
        self.third = third_point

    def square_getter(self):
        length_first = ((self.first.x - self.second.x) ** 2 + (self.first.y - self.second.y) ** 2) ** 0.5
        length_second = ((self.second.x - self.third.x) ** 2 + (self.second.y - self.third.y) ** 2) ** 0.5
        length_third = ((self.third.x - self.first.x) ** 2 + (self.third.y - self.first.y) ** 2) ** 0.5
        half_perimeter = (length_first + length_second + length_third) * 0.5
        square_value = (half_perimeter * (half_perimeter - length_first) * (half_perimeter - length_second) *
                        (half_perimeter - length_third)) ** 0.5
        return square_value

    square = property(square_getter)


if __name__ == '__main__':
    point1 = Point(0, 3)
    point2 = Point(4, 0)
    point3 = Point(5, 0)

    line1 = Line(point1, point2)
    line2 = Line(point2, point3)
    line3 = Line(point3, point1)

    print('first length:', line1.length)
    print('second length:', line2.length)
    print('third length:', line3.length)

    triangle1 = Triangle(point1, point2, point3)
    print('triangle square:', triangle1.square)
