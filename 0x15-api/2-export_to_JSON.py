#!/usr/bin/python3

"""returns information about employee TODO list progress"""

import requests
from sys import argv
import json

if __name__ == "__main__":
    """returns information about employee TODO list progress"""
    if len(argv) > 1:
        url = "https://jsonplaceholder.typicode.com/users"
        user_id = int(argv[1])

        response = requests.get("{}/{}".format(url, user_id))
        name = response.json().get("name")

        if name is not None:
            tasks = requests.get("{}/{}/todos".format(url, user_id))
            tasks = tasks.json()

            all_tasks = {}
            all_tasks.update({user_id: [{"task": task["title"], "completed":
                              task["completed"], "username": name}
                              for task in tasks]})

            with open("{}.json".format(user_id), "w") as f:
                json.dump(all_tasks, f)
