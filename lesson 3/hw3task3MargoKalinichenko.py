
# task3: Існує ліст з різними даними,
# наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сфлрмує новий list (наприклад lst2),
# який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

lst1 = ['1', '2', 909, 3, 6.3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', '']

lst2 = []
for item in lst1:
    if type(item) == int:
        lst2.append(item)
        continue
    elif type(item) == float:
        lst2.append(item)
        continue
print(lst2)