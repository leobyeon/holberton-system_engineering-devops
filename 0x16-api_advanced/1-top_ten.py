#!/usr/bin/python3
"""
queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    print the titles of the 10 hot posts
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
            'user-agent': 'my user agent 1.0',
            'content-type': 'application/json'
            }
    r = requests.get(url, allow_redirects=False, headers=headers)
    if r.status_code != requests.codes.ok:
        print('None')
    else:
        listing = r.json().get('data').get('children')
        return ([print(
            post.get('data').get('title')) for post in listing[:10]])
