# # lesson 3
#
# my_str = 'bacd 1qwre 1dasdf 1fasfd'
#
# result = my_str.split(' ')
#
# print(my_str)
# print(result)
# print(type(result))
#
# my_lst = [1, 2.2, 'T', 1, True, None, [1, 2, 3]]
#
# print(my_lst)
#
# my_lst.append(my_str)
#
# print(my_lst)
#
# my_lst.remove(1)
#
# print(my_lst)
#
# # my_lst.remove(10)
#
# print(1 in my_lst)
# print('T' in my_lst)
# print([1, 2] in my_lst)
#
# print(my_lst)
#
# print(my_lst[1])
# print(my_lst[-1])
# print(my_lst[-3:-1])
#
#
# print(my_str[1])
# # my_str[1] = 'w'
#
# my_lst[1] = '123456789'
# print(my_lst)
#
# my_lst[3] = '123456789'
# print(my_lst)
#
# print(my_lst[1].startswith('2'))
# print(my_lst[5].append(12345))
# print(my_lst)
#
# my_lst.pop(4)
# print(my_lst)

# loop

# while condition: # bool() is True
#     # do smth

# a = 0
# b = 10
# while a < b:
#     print(f'a is {a} b is {b}')
#     a += 1  # a = a + 1

# a = 0
# b = 10
#
# while True:
#     print(f'a is {a} b is {b}')
#     a += 1  # a = a + 1
#     if a >= b:
#         break

# a = 0
# b = 10
#
# while True:
#     a += 1
#     if a % 2 == 0:
#         continue
#
#     print(f'a is {a} b is {b}')
#     if a >= b:
#         break


# lst = [1, 2.2, 'T', 1, True, None, [1, 2, 3]]
#
# idx = 0
#
# while idx < len(lst):
#     print(lst[idx])
#
#     idx += 1

#
# while True:
#     user_input = input('Enter the number: ')
#     if user_input.isdigit():
#         print('Done!')
#         break
#     else:
#         print('It\'s not number!!!')
#

# for loop

# lst = [1, 2.2, 'T', 1, True, None, [1, 2, 3]]
#
# for i in lst:
#     print('--->', i)


# names_lst = ['Bill', 'Bob', 'Joe', 'Tom']
#
# for name in names_lst:
#     if name.lower().startswith('b'):
#         continue
#     print('--->', name)
#     if name[1] == 'o':
#         break


# for char in '1234567890':
#     print('-->', char)

# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9], 'qwertyu']
#
# for value in lst:
#     print('---> ', value)
#
#     for sub_val in value:
#         print('---> --->', sub_val)

# tuple

# my_tuple = (1, 2, 3, 4, 5, 6, 7)
#
# print(my_tuple)
# print(my_tuple[1])
# print(my_tuple[2:5])
#
# # my_tuple[1] = 345
#
# for val in my_tuple:
#     print(f'value is {val}')
#
# my_tuple = (1, '2', 3.2, [2, 3], (2, 3, 4))
# print(my_tuple)
#
#
# my_list = list(my_tuple)
#
# print(my_list)
#
# my_list.append(123)
# print(my_list)
#
# my_tuple = tuple(my_list)
# print(my_tuple)
#
# my_list = list('1234567890-')
# print(my_list)
#
# my_tuple = tuple('1234567890-')
# print(my_tuple)
#
#
# print(bool([1, 3]))
# print(bool([]))
#
# my_list = []
#
# if my_list:
#     print(my_list)

#
# my_list = []
#
# for char in '123sd23asd123sd12sd23':
#     if char.isdigit():
#         my_list.append(char)
#
# print(my_list)
#
# my_list2 = []
#
# for val in my_list:
#     if int(val) % 2 == 0:
#         my_list2.append(val)

# my_list = ['1', '2', '3', '2', '3', '1', '2', '3', '1', '2', '2', '3']
#
#
# list_copy = my_list.copy()
#
# for val in list_copy:  # my_list[:]
#     if int(val) % 2 == 0:
#         my_list.remove(val)
#
# print(my_list)

#
# my_list = [1, 2, 3]
#
#
# my_list += ['2', '3', '4']
#
# print(my_list)
#
# my_list = my_list * 3
#
# print(my_list)
#

#
# my_tuple = (1, '2', 3.2, [2, 3], [],  (2, 3, 4))
#
# print(my_tuple)
#
# my_tuple[3].append(['wertyui', (1, 3, 4)])
#
# print(my_tuple)
#
# my_tuple[3][1] = 1234
#
# print(my_tuple)

# counter = 5
#
# lst = []
# while counter > 0:
#     user_input = input('Enter smth: ')
#     lst.append(user_input)
#     counter -= 1
#
#
# print(lst)

# import time
#
# while True:
#     print('Hello!')
#     time.sleep(120)  # sec


