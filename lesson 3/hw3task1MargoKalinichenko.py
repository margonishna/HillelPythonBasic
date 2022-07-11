# hw3
# task1: Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
# Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".


while True:
    my_str = input("Введіть одне слово: ")
    if len(my_str) == 0:
        print("Пуста строка.")
        continue
    elif not my_str.isalpha():
        print("Не є словом.")
        continue

    my_nmb = input("Введіть номер символа: ")
    if not my_nmb.isdigit():
        print("Не є числом.")
        continue
    int_nmb = int(my_nmb)

    if int_nmb == 0:
        print("Слово немає нульвого елементу")
        continue
    elif len(my_str) < int_nmb:
        print("Слово не таке довге.")
        continue
    else:
        print(f'{my_nmb} символ у слові "{my_str}" це "{my_str[int_nmb-1]}".')
    break





