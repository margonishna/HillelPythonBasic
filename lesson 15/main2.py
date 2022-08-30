class MyProperty:
    def __init__(self, func):
        self._func = func

    def __get__(self, inst, owner=None):
        data = self._func(inst)
        return data


class Location:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @MyProperty
    def loc(self):
        return [self.x, self.y]

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def __ge__(self, other):
        return self.x >= other.x

    def __eq__(self, other):
        return self.x == other.x

    def __gt__(self, other):
        return self.x > other.x


loc = Location()
loc2 = Location()

print(loc >= loc2)
print(loc == loc2)
print(loc <= loc2)
print(loc != loc2)
print(loc < loc2)
print(loc > loc2)

print(loc.loc)
loc.move_left()
loc.move_left()
loc.move_left()
loc.move_left()
print(loc.x)
print(loc.y)
print(loc.loc)
