"""
Підключіться до API НБУ ( документація тут https://bank.gov.ua/ua/open-data/api-dev ),
отримайте курс валют і запишіть його в текстовий файл такому форматі (список):
 "[дата створення запиту]"
1. [назва валюти 1] to UAH: [значення курсу до валюти 1]
2. [назва валюти 2] to UAH: [значення курсу до валюти 2]
3. [назва валюти 3] to UAH: [значення курсу до валюти 3]
...
n. [назва валюти n] to UAH: [значення курсу до валюти n]

P.S.не забувайте про DRY, KISS, SRP та перевірки
"""

import requests
import datetime

url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
date = datetime.date.today()

try:
    result = requests.request('GET', url)
except Exception as error:
    print(error)
else:
    if 300 > result.status_code >= 200:
        if content := result.headers.get('Content-Type'):
            if content == 'application/json; charset=utf-8':
                res_json = result.json()
                res_final_list = [str(date)]
                for number, value in enumerate(res_json, start=1):
                    list_every_currency = str(number) + ". " + value['txt'] + " to UAH: " + str(value['rate'])
                    res_final_list.append(list_every_currency)
                with open('exchange_result.txt', 'wt', encoding='utf-8') as file:
                    file.write('\n'.join(res_final_list))
