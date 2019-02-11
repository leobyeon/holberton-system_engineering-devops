#!/usr/bin/python3
# for a given employee ID, returns information about his/her todo list progress
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    r = requests.get('{}/todos'.format(url))
    try:
        res = r.json()
    except:
        print("Not a valid JSON")

    tasks = []
    completed = []
    for task in res:
        if task["userId"] == int(argv[1]):
            tasks.append(task)
    done = 0
    total = 0
    for task in tasks:
        total += 1
        if task["completed"]:
            done += 1
            completed.append(task)

    u = requests.get('{}/users/{}'.format(url, argv[1]))
    try:
        user = u.json()
        if user:
            print("Employee {} is done with tasks({}/{}):".format(
                user["name"], done, total))
            for task in completed:
                print("\t{}".format(task["title"]))
    except:
        print("Not a valid JSON")
