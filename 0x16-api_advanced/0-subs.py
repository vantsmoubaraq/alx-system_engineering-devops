#!/usr/bin/python3

"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64)'}

    response = requests.get(url, headers=headers).json()
    subscribers = response.get("data", {}).get("subscribers", 0)
    return subscribers
