# humbers

# int, float


# str

# bool
# none

# my_str = '1234567890'
# my_str = "1234567890"
#
#
# my_str = "1234567890" + "asdf"
#
# print(my_str)
#
# name = "Artem"
# age = 38
#
# # Hello, I'm Artem, I'm 38 year old
# str_age = str(age)
# print(type(str_age))
#
# result = "Hello, I'm " + name + ", I'm " + str_age + " year old"
# print(result)
#
# my_int = int("1234")
# print(my_int)
# print(type(my_int))
#
# my_int = int("1234")
# print(my_int)
# print(type(my_int))
#
# my_int = int(2.3333)
# print(my_int)
# print(type(my_int))
#
# my_int = int(True)
# print(my_int)
# print(type(my_int))
#
#
# my_float = float("1234.0")
# print(my_float)
# print(type(my_float))
#
#
# my_bool = bool("1234")
# print(my_bool)
# print(type(my_bool))
#
# my_bool = bool("")
# print(my_bool)
# print(type(my_bool))
#
#
# my_bool = bool(1234)
# print(my_bool)
# print(type(my_bool))
#
# my_bool = bool(-1234)
# print(my_bool)
# print(type(my_bool))
#
# my_bool = bool(-1234.0)
# print(my_bool)
# print(type(my_bool))
#
# my_bool = bool(0)
# print(my_bool)
# print(type(my_bool))
#
# my_bool = bool(None)
# print(my_bool)
# print(type(my_bool))


# name = "Artem"
# age = 38
#
# result = "Hello, I'm " + name + ", I'm " + str(age) + " year old"
# print(result)
#
# result = "Hello, I'm %s, I'm %s year old" % (name, age)
# print(result)
#
# result = "Hello, I'm %s, I'm %s year old" % (age, name)
# print(result)
#
# result = "Hello, I'm {}, I'm {} year old".format(name, age)
# print(result)
#
# tpl = "Hello, I'm {}, I'm {} year old"
# result = tpl.format(name, age)
# print(result)
#
#
# tpl = "Hello, I'm {name}, I'm {age} year old"
# result = tpl.format(name=name, age=age)
# print(result)
#
# result = tpl.format(age=name, name=age)
# print(result)
#
# tpl = "Hello, I'm {}, I'm {} year old"
# result = tpl.format(name, age)
# print(result)
#
# # F-string
#
# result = f"Hello, I'm {name}, I'm {age ** 2} year old"
# print(result)
#
# result = F"Hello, I'm {name}, I'm {age ** 2} year old"
# print(result)
#
# # string methods

#
# my_string = '123456 abcdefgh 987654'
#
# result = my_string.replace('5', '++')
# print(result)
#
# result = my_string.replace('56', '++')
# print(result)
#
#
# my_string = '--123456 abcd - efgh 987654--'
# print(my_string)
# result = my_string.strip('-')
# print(result)
#
# result = my_string.lstrip('-')
# print(result)
#
# result = my_string.rstrip('-')
# print(result)
#
# my_string = '--123456 abcd - EFGH 987654--'
# print(my_string)
#
# result = my_string.upper()
# print(result)
#
# result = my_string.lower()
# print(result)
#
# result = my_string.title()
# print(result)
#
# my_string = 'abcd - EFGH \n 987654--'
# result = my_string.capitalize()
# print(result)
#
# my_string = '123456 abcd - EFGH \n 987654 56--'
# result = my_string.count('56')
# print(result)
#
# my_string = '0123456 abcd - EFGH \n 987654 56--'
# result = my_string.startswith('12')
# print(result)
#
# my_string = '0123456 abcd - EFGH \n 987654 56'
# result = my_string.endswith(' 56')
# print(result)
#
# my_string = '012345656'
# result = my_string.isdigit()
# print(result)
#
# my_string = '012345656'
# result = my_string.isalpha()
# print(result)
#
# my_string = '012345656sdfghjk'
# result = my_string.isalnum()
# print(result)


# if else

# if condition:
#     do smth
# else:
#     do smth else
#
# condition = False
#
# print('Before')
#
# if condition:  # bool(condition) is True
#     print('Yes')
#     print('Yes')
#     print('Yes')
# else:
#     print('No')
#     print('No')
#     print('No')
#
# print('After')
#
#
# my_str = '123567'
#
# if my_str.isdigit():  # bool() is True
#     print('It is digit !!!!!')
#     print('It is digit !!!!!')
#     if my_str.startswith('1'):
#         print('It starts with 1')
# else:
#     print('It is not digit !!!!!')
#
# if my_str.startswith('1'):
#     print('It starts with 1')

# my_str = '123567'
# result = my_str.isdigit()

# if result:  # bool() is True
#     print('It is digit !!!!!')
# elif my_str.isalpha():
#     print('It is letters !!!!!')
# elif 1 > 2:
#     print('1 > 2')
# else:
#     print('It is not digit !!!!!')


# my_str = '123567'
#
# if my_str.isdigit():  # bool() is True
#     print('It is digit !!!!!')
# elif my_str.isalpha():
#     print('It is letters !!!!!')
# elif 1 > 2:
#     print('1 > 2')
#
#
# my_str = '0123456789'
# print(my_str.find('5'))
#
# print(my_str.find('12'))

my_str = '0123456789'
print(my_str[0])
print(my_str[9])
# print(my_str[10])

print(my_str[-1])
print(my_str[-3])

print(my_str)
print('my_str[1:6]', my_str[1:6])
print('my_str[6:8]', my_str[6:8])
print('my_str[4:-2]', my_str[4:-2])
print('my_str[-6:-2]', my_str[-6:-2])
print('my_str[-1:-7]', my_str[-1:-7])
print('my_str[3:]', my_str[3:])
print('my_str[:7]', my_str[:7])
print('my_str[1:8:3]', my_str[1:8:3])
print('my_str[-1:-8:-1]', my_str[-1:-8:-1])
print('my_str[len(my_str)//2:]', my_str[len(my_str)//2:])


print(my_str[:2], my_str[5:])




