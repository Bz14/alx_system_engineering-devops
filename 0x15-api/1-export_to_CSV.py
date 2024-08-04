#!/usr/bin/python3
""" A module to gather data from an API"""
import csv
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
            file_name = "{}.csv".format(id)
            with open(file_name, mode="w", newline='', encoding='utf-8') as file:
                csv_writer = csv.writer(file)
                for task in todos:
                    username = data.get("username")
                    completed = task.get("completed")
                    title = task.get("title")
                    csv_writer.writerow([id, username, completed, title])
                
