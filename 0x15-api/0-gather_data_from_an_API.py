#!/usr/bin/python3
""" A module to gather data from an API"""
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(id)
    response = requests.get(employee_url)
    if response.status_code == 200:
        data = response.json()
        name = data.get("name")
        response = requests.get(url)
        if response.status_code == 200:
            todos = response.json()
            t = len(todos)
            completed_task = [task for task in todos if task.get("completed")]
            n = len(completed_task)
            st = "Employee {} is done with tasks({}/{}):".format(name, n, t)
            print(st)
            for task in completed_task:
                print("\t {}".format(task.get("title")))
