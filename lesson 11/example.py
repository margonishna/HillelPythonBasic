# OOP

# Abstraction
# Encapsulation
# Inheritance
# Polymorphism


# do_smth_good
#
# class User:  # CamelCase
#     pass
#
#
# user = User()
#
# print(type(1))
# print(type(user))
#
# print(isinstance(1, int))
# print(isinstance(user, User))

#
# class User:
#
#     name = 'Bill'
#     age = 30
#
#
# user1 = User()
# user2 = User()
#
# print(type(user1))
# print(user1.name)
# print(user1.age)
# # print(user1.address)
#
# user2.name = 'Tom'
# user2.age = 20
#
# print(user2.name)
# print(user2.age)
#
# user2.address = 'Odessa Deribasovsrska str'
# print(user2.address)
# # print(user1.address)

#
# class User:
#
#     name = 'Bill'
#     age = 30
#
#     def say_hello(self):  # self = object
#         return f'Hello, my name is {self.name}, I\'m {self.age} year old'
#
#     def say_hello2(self, prefix):  # self = object
#         return f'{prefix}, my name is {self.name}, I\'m {self.age} year old'
#
#
# user1 = User()
# user2 = User()
#
# print(user1.say_hello())
# user1.name = 'Tom'
# user1.age = 100
#
# # print(User.say_hello(user1))
# print(user1.say_hello())  # User.say_hello(user1)
#
# print(user1.say_hello2('Hi!'))
#
# print(user2.say_hello())
#
#
# class User:
#     name = 'Bill'
#     age = 30
#
#     def say_hello(self):  # self = object
#         return f'Hello, my name is {self.name}, I\'m {self.age} year old'
#
#
# user1 = User()
#
# print(dir(user1))
#
# user1.address = 'Odessa'
# print(dir(user1))
#
#
# res = hasattr(user1, 'address')
# print(res)
#
# res = hasattr(user1, 'salary')
# print(res)
#
# user1 = User()
#
# arrtname = 'address'
# # user1.arrtname = 'Odessa'
#
# setattr(user1, 'address', 'Odessa')  # user1.address = 'Odessa'
# setattr(user1, arrtname, 'Odessa')  # user1.address = 'Odessa'
#
#
# user1 = User()
#
#
# arrtname = 'address'
#
# res = user1.name  # str
# print(res)
#
# res = getattr(user1, arrtname, None)
# # res = user1.arrtname  # str
#
# print(res)
#
# user2 = User()
#
# user2.age = 100
# print(user2.age)
#
# res = delattr(user2, 'age')
#
# print(user2.age)
#
#
# class User:
#     name = None
#     age = None
#
#     def __init__(self, new_name, new_age):
#         print(f'in init {self.name} {self.age}')
#         self.name = new_name
#         self.age = new_age
#         print(f'in init {self.name} {self.age}')
#
#     def say_hello(self):  # self = object
#         return f'Hello, my name is {self.name}, I\'m {self.age} year old'
#
#
# user = User(new_name='Tom', new_age=50)
# print(user.say_hello())
#
# user1 = User(new_name='Duncan', new_age=420)
# print(user1.say_hello())
#
# user2 = User(new_name='Joe', new_age=20)
# print(user2.say_hello())

#
# class User:
#     name = None
#     age = None
#     _phone = None  # protected
#     __address = None  # private
#
#     def __init__(self, new_name, new_age, new_phone, new_address):
#         print(f'in init {self.name} {self.age}')
#         self.name = new_name
#         self.age = new_age
#         self._phone = new_phone
#         self.__address = new_address
#
#         print(f'in init {self.name} {self.age}')
#
#     def say_hello(self):  # self = object
#         return f'Hello, my name is {self.name}, I\'m {self.age} year old. My phone is {self._phone}. ' \
#                f'My address is {self.__address}'
#
#
# user = User(new_name='Tom', new_age=50, new_phone='+380631231212', new_address='Odessa')
#
# user.name = [1, 2, 3]
# print(user.say_hello())
# print('protected', user._phone)
# # print('private', user.__address)
# print('private', user._User__address)  #


# class User:
#     name = None
#     age = None
#     address = None
#
#     def __init__(self, new_name, new_age, address):
#
#         self.name = new_name
#         self.age = new_age
#         self.address = address
#
#     def say_hello(self):  # self = object
#         return f'Hello, my name is {self.name}, I\'m {self.age} year old.'
#
#
# class Programmer:
#     name = None
#     age = None
#     language = None
#
#     def __init__(self, new_name, new_age, lang):
#         self.name = new_name
#         self.age = new_age
#         self.language = lang
#
#     def say_hello(self):  # self = object
#         return f'Hello, my name is {self.name}, I\'m {self.age} year old.'
#
#
# pr = Programmer('Bill', 50, 'C++')
#
# print(dir(pr))


# class User(object):  # 2.7

class User:
    name = None
    age = None
    address = None

    def __init__(self, new_name, new_age, address):
        self.name = new_name
        self.age = new_age
        self.address = address

    def say_hello(self):
        return f'Hello, my name is {self.name}, I\'m {self.age} year old.'


class Programmer(User):
    language = None

    def say_hello(self):
        return f'Hello, my name is {self.name}, I\'m {self.age} year old. ' \
               f'Language is {self.language}'


user = User('Bill', 50, 'Odessa')

pr = Programmer('Bill', 50, 'Odessa')

print(dir(pr))
print(pr.name)
print(pr.age)
print(pr.language)

print(user.say_hello())
print(pr.say_hello())


print(Programmer.mro())


print(isinstance(pr, Programmer))
print(isinstance(pr, User))
print(isinstance(user, Programmer))


print(isinstance(True, int))
