#!/usr/bin/python3
""" A module to gather data from an API"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_url = "https://jsonplaceholder.typicode.com/users"
    url = "https://jsonplaceholder.typicode.com/todos?userId={}"
    json_data = {}
    response = requests.get(employee_url)
    if response.status_code == 200:
        data = response.json()
        for user in data:
            username = user.get("username")
            id = user.get("id")
            url = url.format(id)
            response = requests.get(url)
            if response.status_code == 200:
                todos = response.json()
                res = []
                for task in todos:
                    completed = task.get("completed")
                    title = task.get("title")
                    res.append({
                        "username": username,
                        "task": title,
                        "completed": completed
                    })
                json_data[id] = res
                file = "todo_all_employees.json"
                with open(file, mode="w", encoding='utf-8') as f:
                    json.dump(json_data, f)
