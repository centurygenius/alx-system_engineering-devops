#!/usr/bin/python3
"""
    Module to querry Reddit API and return total number
    of subscribers.
"""

import requests

def number_of_subscribers(subreddit):
    """Method queries the Reddit API and returns the number of subscribers"""

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
