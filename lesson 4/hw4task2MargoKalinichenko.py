"""
Завдання 2
макс 30 балів
дано код Морзе, що зберігається в словнику
є стрічка, в якій слова розділені 2 пробілами, а букви в слові - одним пробілом
написати програму по декодуванню даної (чи подібної) стрічки
ПІДКАЗКА - при потребі можна створити симетричний словник, де ключами буде код Морзе, а значеннями - символи латиниці
"""
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

string_to_decode1 = '..  .-.. .. -.- .  .--. -.-- - .... --- -.  ...-- .-.-.- .---- ----- '
string_to_decode2 = '..  -.- -. --- .-- --..--  -.-- --- ..-  -.-. .- -.  -.. ---  .. - '

MORSE_NEW = {}

for key in MORSE_CODE_DICT:
    MORSE_NEW[MORSE_CODE_DICT[key]] = key


list_words_str1 = string_to_decode1.split('  ')
my_str1 = ''

for word in list_words_str1:
    word_lst = word.split()
    for letter in word_lst:
        my_str1 += MORSE_NEW[letter]
    my_str1 += ' '

my_str1 = my_str1.rstrip()
print(my_str1)


list_words_str2 = string_to_decode2.split('  ')
my_str2 = ''

for word in list_words_str2:
    word_lst = word.split()
    for letter in word_lst:
        my_str2 += MORSE_NEW[letter]
    my_str2 += ' '

my_str2 = my_str2.rstrip()
print(my_str2)