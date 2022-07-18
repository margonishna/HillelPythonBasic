"""
завантажити використовуючи requests структуру даних з
https://dummyjson.com/todos
та вивести на екран не виконані значення todo з тих даних, які до вас прийшли
"""
import requests
from pprint import pprint

url = 'https://dummyjson.com/todos'
todo_raw = requests.get(url)
todo_ready = todo_raw.json()
# pprint(todo_ready)

list_todo_not_completed = [todo_ready['todos'][x]['todo'] for x in range(todo_ready['limit']) if not todo_ready['todos'][x]['completed']]
print("Незавершені завдання:")
pprint(list_todo_not_completed)