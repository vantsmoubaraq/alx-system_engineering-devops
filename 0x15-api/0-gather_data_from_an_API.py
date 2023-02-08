#!/usr/bin/python3

"""returns information about employee TODO list progress"""

import requests
from sys import argv

if __name__ == "__main__":
    """returns information about employee TODO list progress"""
    if len(argv) > 1:
        url = "https://jsonplaceholder.typicode.com/users"
        user_id = int(argv[1])

        response = requests.get("{}/{}".format(url, user_id))
        name = response.json().get("name")

        if name is not None:
            tasks = requests.get("{}/{}/todos".format(url, user_id))
            number_of_tasks = len(tasks.json())

            completed_tasks = []
            for task in tasks.json():
                if task.get("completed") is True:
                    completed_tasks.append(task.get("title"))

            number_of_complete = len(completed_tasks)

            print("Employee {} is done with tasks({}/{}):".format(name,
                  number_of_complete, number_of_tasks))
            for task in completed_tasks:
                print("\t {}".format(task))
