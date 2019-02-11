#!/usr/bin/python3
# exports data in the CSV format
import csv
import requests
from sys import argv


def one():
    url = 'https://jsonplaceholder.typicode.com'
    n = requests.get('{}/users/{}'.format(url, argv[1])).json()
    uid = int(argv[1])
    name = n['username']
    all_t = requests.get('{}/todos'.format(url)).json()
    tasks = [t for t in all_t if t['userId'] == uid]
    objs = [{'id': argv[1],
             'name': name,
             'completed': t.get('completed'),
             'title': t.get('title')} for t in tasks]
    with open('{}.csv'.format(argv[1]), mode='w') as f:
        fieldnames = ['id', 'name', 'completed', 'title']
        writer = csv.DictWriter(
                f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writerows(objs)

if __name__ == "__main__":
    one()
