#!/usr/bin/python3
# exports data in JSON format
import requests
import json
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    n = requests.get('{}/users/{}'.format(url, argv[1])).json()
    uid = int(argv[1])
    name = n['username']
    all_t = requests.get('{}/todos'.format(url)).json()
    tasks = [t for t in all_t if t['userId'] == uid]
    objs = [{'task': t.get('title'),
             'completed': t.get('completed'),
             'username': name} for t in all_t]
    form = {str(uid): objs}
    with open('{}.json'.format(argv[1]), mode='w') as f:
        json.dump(form, f)
