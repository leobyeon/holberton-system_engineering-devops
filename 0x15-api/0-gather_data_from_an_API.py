#!/usr/bin/python3
# for a given employee ID, returns information about his/her todo list progress
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    all_t = requests.get('{}/todos'.format(url)).json()
    uid = int(argv[1])
    tasks = [t for t in all_t if t['userId'] == uid]
    completed = [c for c in tasks if c['completed'] is True]
    total = len(tasks)
    done = len(completed)

    u = requests.get('{}/users/{}'.format(url, argv[1]))
    try:
        user = u.json()
        if user:
            print("Employee {} is done with tasks({}/{}):".format(
                user["name"], done, total))
            for task in completed:
                print("\t {}".format(task["title"]))
    except:
        print("Not a valid JSON")
