"""
Доопрацюйте класс Triangle з попередньої домашки наступним чином:
обʼєкти классу Triangle можна порівнювати між собою (==, !=, >, >=, <, <=)
print() обʼєкту классу Triangle показує координати його вершин
print(triangle1)
> (Point(1,0) Point(5,9) Point(3,3))
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

    def __eq__(self, other):
        if self.square == other.square:
            return True
        return False

    def __en__(self, other):
        if self.square != other.square:
            return True
        return False

    def __lt__(self, other):
        if self.square < other.square:
            return True
        return False

    def __le__(self, other):
        if self.square <= other.square:
            return True
        return False

    def __gt__(self, other):
        if self.square > other.square:
            return True
        return False

    def __ge__(self, other):
        if self.square >= other.square:
            return True
        return False

    def __repr__(self):
        point_coord1 = (self._first.x, self._first.y)
        point_coord2 = (self.second.x, self.second.y)
        point_coord3 = (self.third.x, self.third.y)
        return f'(Point1{point_coord1} Point2{point_coord2} Point3{point_coord3})'


if __name__ == '__main__':
    point1 = Point(0, 3)
    point2 = Point(4, 0)
    point3 = Point(5, 0)
    point4 = Point(4, 4)

    triangle1 = Triangle(point1, point2, point3)
    square1 = triangle1.square
    print('square1:', square1)

    triangle2 = Triangle(point1, point2, point3)
    square2 = triangle2.square
    print('square2:', square2)

    triangle3 = Triangle(point1, point2, point4)
    square3 = triangle3.square
    print('square3:', square3)

    print('square1 == square2:', square1 == square2)
    print('square1 == square3:', square1 == square3)

    print('square1 != square3:', square1 != square3)
    print('square1 != square2:', square1 != square2)

    print('square1 < square3:', square1 < square3)
    print('square1 < square2:', square1 < square2)

    print('square1 <= square3:', square1 <= square3)
    print('square1 <= square2:', square1 <= square2)
    print('square3 <= square1:', square3 <= square1)

    print('square1 > square3:', square1 > square3)
    print('square3 > square2:', square3 > square2)

    print('square1 >= square3:', square1 >= square3)
    print('square1 >= square2:', square1 >= square2)
    print('square3 >= square1:', square3 >= square1)

    print('triangle1 points:', triangle1)
    print('triangle2 points:', triangle2)
    print('triangle3 points:', triangle3)
