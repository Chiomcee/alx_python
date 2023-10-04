#!/usr/bin/python3
"""
    Exports all tasks from all employees in JSON format.
"""


import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{api_url}/users/{user_id}"
    todos_url = f"{user_url}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200:
        print("User not found")
        sys.exit()

    user_data = user_response.json()
    todos_data = todos_response.json()

    todo_dict = {str(user_id): []}

    for todo in todos_data:
        task_dict = {
            "username": user_data.get("username"),
            "task": todo.get("title"),
            "completed": todo.get("completed"),
        }
        todo_dict[str(user_id)].append(task_dict)

    with open(f"{user_id}.json", "w") as json_file:
        json.dump(todo_dict, json_file)