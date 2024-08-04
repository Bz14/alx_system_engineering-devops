#!/usr/bin/python3
""" A module to gather data from an API"""
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    response = request.get(url)
    if response.status_code == 200:
        data = responce.json()
        print(data)
