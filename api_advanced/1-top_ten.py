#!/usr/bin/python3
"""
Reddit API Query Module

This module contains a function that retrieves and prints the titles of the top 
10 hot posts from a given subreddit using Reddit's API.

Functions:
    - top_ten(subreddit): Fetches and prints the top 10 post titles.
"""

import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints the top 10 post titles, or 'None' if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "ALX-Reddit-Query"}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print("None")
        return
    
    try:
        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print("None")
            return
        
        for post in posts:
            print(post["data"]["title"])
    
    except Exception:
        print("None")
