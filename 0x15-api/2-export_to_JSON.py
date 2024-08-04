#!/usr/bin/python3
""" A module to gather data from an API"""
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(id)
    response = requests.get(employee_url)
    if response.status_code == 200:
        data = response.json()
        username = data.get("username")
        response = requests.get(url)
        if response.status_code == 200:
            todos = response.json()
            json_data = {}
            res = []
            for task in todos:
                completed = task.get("completed")
                title = task.get("title")
                res.append({
                        "task": title,
                        "completed": completed,
                        "username": username
                })
            json_data[id] = res
            file = "{}.json".format(id)
            with open(file, mode="w", encoding='utf-8') as f:
                json.dump(json_data, f)
