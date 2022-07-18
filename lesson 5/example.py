######################
# тернарний оператор #
######################

# classic if-else statement
# a = 1
# b = 3
#
# if a > b:
#     print(a)
# else:
#     print(b)

# ternar operator (one-line alternative)

#     variable 1    condition   alternative variable
# print(a  if          a > b      else             b if b % 2 == 0 else 'none')
# print(a if a > b else b)


######################
# comprehension #
######################


# my_list = []
# for number in range(10):
#     my_list.append(number)

# important []
# my_list = [number if number % 2 == 0 else "none" for number in range(10)] # redundant data
# my_list = [number for number in range(10) if number % 2 == 0]
# my_list1 = [item for item in [2, 3.5, []]]
# print(my_list)
# print(my_list1)

# important {}

# my_set = {number for number in range(10) if number % 2 == 0}
# my_set1 = {number for number in '11112445454544' if int(number) % 2 == 0}
# print(my_set)
# print(my_set1)
#
# my_dict = {number: number for number in range(10) if number % 2 == 0}
# my_dict1 = {number: int(number) for number in '11112445454544' if int(number) % 2 == 0}
# my_dict2 = {number: {number: int(number), 'name': 'Igor'} for number in '11112445454544' if int(number) % 2 == 0}
# print(my_dict)
# print(my_dict1)
# print(my_dict2)

# one-time use
# mu_generator = (number for number in range(10000000000000000) if number % 2 == 0)
# print(mu_generator)
# print(next(mu_generator))
# print(next(mu_generator))
# print(next(mu_generator))
# print(next(mu_generator))



# practic

# pip install requests
# import requests
# from pprint import pprint
# url = 'http://api.open-notify.org/astros.json'
# asto_raw = requests.get(url)

# asto_ready = asto_raw.json()
#
#
# pprint(asto_ready)
# print()
#
# list_astos_in_space = [asto_ready['people'][x]['name'] for x in range(asto_ready['number'])]
# for i in range(asto_ready['number']):
#     print(asto_ready['people'][i]['name'])

# pprint(asto_ready['people'][0])
# pprint(list_astos_in_space)
# print()
#
# astro_craft_set = {asto_ready['people'][x]['craft'] for x in range(asto_ready['number'])}
# print(astro_craft_set)
# print('*'*50)

# for key in asto_ready:
#     print(key)
#     if type(asto_ready[key]) == list:
#         for item in asto_ready[key]:
#             for i in item:
#                 print(item[i])


#
student = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 21,
        'Номер телефону': '+380987771221',
        'Середній бал': None,
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 22,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}
#
# for stud in student:
#     if not student[stud]['Номер телефону']:
#         student[stud]['Номер телефону'] = '0986545454552'

# pprint(student)

# student['Василь Картичак'] = {
#         'Пошта': 'Masha@gmail.com',
#         'Вік': 18,
#         'Номер телефону': '+380986671221',
#         'Середній бал': 80
#     }

# student['Василь Картичак'] = {}
# student['Василь Картичак']['hobby'] = 'tennis'

#
# pprint(student)
# pprint(len(student))

# for stud in student:
#     print(student[stud].setdefault('Середній бал', 50))

# print(hash('Середній бал'))



# print(hash(student)) # error


######################################### HOMEWORK
# phones_url = 'https://dummyjson.com/products/category/smartphones'
# responce = requests.get(phones_url)
# clean_data = responce.json()
#
# pprint(clean_data['products'])

# total_stock = 0
#
# for i in range(len(clean_data['products'])):
#     # pprint(clean_data['products'][i])
#     if clean_data['products'][i]['brand'] == "Apple":
#         total_stock += clean_data['products'][i]['stock']
#
#         picture_url = clean_data['products'][i]['thumbnail']
#         picture = requests.get(picture_url)
#         out = open(f"{clean_data['products'][i]['title']}.jpg", 'wb')
#         out.write(picture.content)
#         out.close()
#
# print(total_stock)


###############################################
# weird task

# {"Igor": {"bread": 3, "plate": 2}, "Olena": {"bread": 1} }

# sales = {}
# while True:
#     customer = input('Next client >>> ')
#     if customer == 'no more':
#         break
#
#     name, item, amount, *_ = customer.split()
#     sales[name][item] = sales.setdefault(name, {}).setdefault(item, 0) + int(amount)

# print(sales)


# for stud in student:
#     # if not student[stud]['Середній бал']:
#     #     raise ValueError
#
#     print(student[stud]['Середній бал'])

dict_1 = {'1': 'one'}
dict_2 = {}
for i in dict_1:
    print(i)
    dict_2[dict_1[i]] = i

print(dict_2)
dict_1.update(dict_2)
print(dict_1)
