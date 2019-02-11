#!/usr/bin/python3
# exports data in JSON format: dict of list of dicts
import requests
import json
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    all_u = requests.get('{}/users'.format(url)).json()
    form = {}
    name = [n['username'] for n in all_u]
    all_t = requests.get('{}/todos'.format(url)).json()
    for u in all_u:
        uid = u.get('id')
        name = u.get('username')
        tasks = [t for t in all_t if t['userId'] == uid]
        objs = [{'username': name,
                 'task': t.get('title'),
                 'completed': t.get('completed')} for t in all_t]
        form[str(uid)] = objs
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(form, f)
