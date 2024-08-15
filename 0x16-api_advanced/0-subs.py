#!/usr/bin/python3
""" A function to query from an api """

import requests


def number_of_subscribers(subreddit):
    """ Return the total number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozzilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    return 0
