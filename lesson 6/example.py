# functions

# def my_func(arg):
#     print('Hello, i\'m a function')
#     print(arg)
#     return 1
#
# # res = my_func('12345')
#
#
# def my_sum(arg_1, arg_2):
#     print('Hello, i\'m a function `my_sum`')
#     result = arg_1 + arg_2
#     return result
#
#
# result = my_sum(2, 3)
# print(result)

#
# def my_sum(arg_1, arg_2):
#     print('Hello, i\'m a function `my_sum`')
#     result = arg_1 + arg_2
#     return result
#
#
# result = my_sum(2, 3)
# print(result)
#
#
# result = my_sum(3, 2)
# print(result)
#
#
# result = my_sum(arg_1=3, arg_2=2)
# print(result)
#
#
# result = my_sum(arg_2=2, arg_1=3)
# print(result)


# def my_sum(arg_1, arg_2, arg_3):
#     print('Hello, i\'m a function `my_sum`')
#     print(f'arg_1 {arg_1}, arg_2 {arg_2}, arg_3 {arg_3}')
#     result = arg_1 + arg_2 + arg_3
#     return result
#
#
# result = my_sum(1, 2, 3)
# print(result)
#
# result = my_sum(3, 2, 1)
# print(result)
#
# result = my_sum(arg_2=3, arg_3=2, arg_1=1)
# print(result)
#
# result = my_sum(1, arg_3=2, arg_2=3)
# print(result)
#
# result = my_sum(arg_1=1, arg_2=3, arg_3=2)
# print(result)
#
# x = 10
# y = 20
#
# result = my_sum(arg_1=result, arg_2=x, arg_3=y)
# print(result)

#
# def my_sum(arg_1, arg_2, arg_3):
#     print('Hello, i\'m a function `my_sum`')
#     print(f'arg_1 {arg_1}, arg_2 {arg_2}, arg_3 {arg_3}')
#     result = arg_1 + arg_2 + arg_3
#     return result
#
#
# result = my_sum(1, 1, 1)
#
# print(result)


# def my_sum(arg_1, arg_2, arg_3):
#     print('Hello, i\'m a function `my_sum`')
#     print(f'arg_1 {arg_1}, arg_2 {arg_2}, arg_3 {arg_3}')
#     return arg_1 + arg_2 + arg_3
#
#
# result = my_sum(1, 1, 1)
#
# print(result)


# def my_sum(arg_1, arg_2, arg_3):
#     print('Hello, i\'m a function `my_sum`')
#
#     return arg_1 + arg_2 + arg_3
#     print(f'arg_1 {arg_1}, arg_2 {arg_2}, arg_3 {arg_3}')
#
#
# result = my_sum(1, 1, 1)
#
# print(result)


# def my_div(arg_1, arg_2):
#     print(f'args {arg_1} {arg_2}')
#
#     if arg_2 == 0:
#         print(f'arg_2 is {arg_2}')
#         return 0
#
#     result = arg_1 / arg_2
#     print(f'result is {result}')
#     return result
#
#
# result = my_div(1, 2)
#
# print(result)


# def my_div(arg_1=1, arg_2=1):
#     print(f'args {arg_1} {arg_2}')
#
#     if arg_2 == 0:
#         print(f'arg_2 is {arg_2}')
#         return 0
#
#     result = arg_1 / arg_2
#     print(f'result is {result}')
#     return result
#
#
# result = my_div(4, 2)
#
# print(result)
#
#
# result = my_div(arg_2=10)
#
# print(result)

#
# def list_updater(data_to_add, list_to_update):
#     list_to_update.append(data_to_add)
#     return list_to_update
#
#
# lst = [1, 2, 3]
# print(lst)
#
# lst = list_updater('asd', lst)
# print(lst)
#
#
# def list_updater(data_to_add, list_to_update=[]):
#     list_to_update.append(data_to_add)
#     return list_to_update
#
#
# lst = list_updater('abcd', lst)
# print(lst)
#
# print(list_updater('abcd'))
#
# print(list_updater(1, lst))
#
# print(list_updater(1))
#
#
# def list_updater(data_to_add, list_to_update=None):
#     if list_to_update is None:
#         list_to_update = []
#
#     list_to_update.append(data_to_add)
#     return list_to_update
#
#
# print(list_updater(1))
# print(list_updater(1))

# lst = [1, 2, 3, 4]
#
#
# def list_updater(data_to_add, list_to_update):
#
#     list_to_update.append(data_to_add)
#
#     return list_to_update
#
#
# print(lst)
#
# lst = list_updater('abcd', lst)
#
# print(lst)


# namespaces

#
# def foo(arg1, x):
#
#     print(f'arg1 {arg1}')
#
#     print(f'x {x}')
#
#     return


# x = 10

# foo(123)

# print(x)


x = 10


def foo(arg1):

    print(f'arg1 {arg1}')
    global x
    # x = 100
    print(f'x {x}')
    x = 100

    return


print('before function call', x)

foo(123)

print('after function call', x)


def foo(arg1, arg2):

    print(f'arg1 {arg1}')
    # x = 100
    print(f'x {arg2}')
    arg2 = 100

    return arg2


x = foo(123, x)

