#!/usr/bin/python3

"""queries the Reddit API and prints the titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """queries the Reddit API"""
    if subreddit is None or type(subreddit) is not str:
        print(None)
        return
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False).json()
    [print(child.get("data").get("title")) for child in
     response.get("data").get("children")]
