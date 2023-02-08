#!/usr/bin/python3

"""returns information about employee TODO list progress"""

import requests
from sys import argv
import csv

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

            with open("{}.csv".format(user_id), "w", newline="") as f:
                file_write = csv.writer(f)
                for task in tasks:
                    file_write.writerow([user_id, name, task.get("completed"),
                                        task.get("title")])
