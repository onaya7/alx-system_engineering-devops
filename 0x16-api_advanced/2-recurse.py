#!/usr/bin/python3
"""
Query Reddit API to find top 10 hot posts of a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Prints the titles of first 10 hot posts for a given subreddit

    Args:
        subreddit (str): Subreddit name to query Reddit API
    """
    headers = {'User-Agent': 'Holberton Student 329'}
    check_url = 'https://reddit.com/api/search_reddit_names.json'
    params = {'query': subreddit, 'exact': True}
    check = requests.get(check_url, headers=headers, params=params)
    if check.status_code != 200 or len(check.json()['names']) is 0:
        return []
    url = 'https://reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {'limit': 100, 'after': after}
    sr = requests.get(url, headers=headers, params=params)
    hot_posts = sr.json().get('data').get('children')
    hot_list.extend([x.get('data').get('title') for x in hot_posts])
    after = sr.json().get('data').get('after')
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
