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
            'user-agent': 'my user agent 1.0',
            'content-type': 'application/json'
            }
    if after:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
                subreddit, after)
    else:
        url = 'https://www.reddit.com/r/{}/hot'.format(subreddit)
    try:
        r = requests.get(url, allow_redirects=False, headers=headers).json()
        after = r.get('data').get('after')
        posts = r.get('data').get('children')
        hot_list = [post.get('data').get('title') for post in posts]
        if not after:
            return (hot_list)
        return (recurse(subreddit, hot_list, after))
    except:
        return (None)
