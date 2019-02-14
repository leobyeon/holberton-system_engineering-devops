#!/usr/bin/python3
"""
queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    return a list of titles of all hot article
    """
    headers = {
            'user-agent': 'my user'
            }
    if after:
        url = 'https://api.reddit.com/r/{}/hot?after={}'.format(
                subreddit, after)
    else:
        url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            return (None)
        after = r.json().get('after')
        posts = r.json().get('data').get('children')
        for post in posts:
            hot_list.append(post.get('data').get('title'))
        if not after:
            return (hot_list)
        return (recurse(subreddit, hot_list, after))
