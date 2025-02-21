#!/usr/bin/python3
""" 1-top_ten.py - Fetch and print the top 10 hot posts of a subreddit. """

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'MyRedditApp/0.1 by YourUsername'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check for valid response
    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if not posts:
            print(None)
            return
        for post in posts:
            print(post['data'].get('title', ''))
    except (KeyError, ValueError):
        print(None)
