# task2: Вести з консолі строку зі слів за допомогою input()
# (або скористайтеся константою).
# Напишіть код, який визначить кількість слів, в цих даних.


print("Введіть декілька слів:")
my_str = input()
my_lst = my_str.split(' ')

count_str = 0

for word in my_lst:
    if word == '':
        my_lst.remove(word)
        continue
    elif not word.isalpha():
        continue
    elif type(word) == str:
        count_str += 1

if len(my_lst) == 0:
    print("Пусто, введіть щось.")

print(f'Кількість слів: {count_str}')
