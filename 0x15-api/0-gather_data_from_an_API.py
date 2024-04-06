#!/usr/bin/python3
"""Gather data from an API"""

import requests 
from sys import argv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    u_id = argv[1]
    user = requests.get(url + "users/{}".format(u_id).json())
    todo = requests.get(url + "todo", params={"userid":u_id}).json()
    complete = [task for task in todo if task.get("complete") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(complete), len(todo)))
    for task in complete:
        print("\t {}".format(task.get("title")))



