#!/usr/bin/python3
# returns the number of subscribers to a subreddit
import requests


def number_of_subscribers(subreddit):
    """ grabs the number of total subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
            'user-agent': 'my user agent 1.0',
            'content-type': 'application/json'
            }
    r = requests.get(url, allow_redirects=False, headers=headers)
    if r.status_code != requests.codes.ok:
        return (0)
    return (r.json().get('data').get('subscribers'))
