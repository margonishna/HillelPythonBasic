class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('jhghjgjgjghg')

    def __set_name__(self_int, owner, name: str):
        self_int.name = '_' + name

    def __get__(self_int, instance, owner):
        return getattr(instance, self_int.name)

    def __set__(self_int, instance, value):
        self_int.verify_coord(value)
        setattr(instance, self_int.name, value)

    # костиль
    # def __get__(self_int, instance, owner):
    #     return instance.__dict__[self_int.name]
    #
    # def __set__(self_int, instance, value):
    #     print('setter ;ljjl;j')
    #     self_int.verify_coord(value)
    #     instance.__dict__[self_int.name] = value

class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

p = Point3D(2, 2, 3)
print(p.__dict__)
