#!/usr/bin/python3
"""
   Module that access API of user's todo-list
"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_ID = int(sys.argv[1])
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users/{employee_ID}'
    todo_url = f'{base_url}/todos?userId={employee_ID}'

    try:
        user_response = requests.get(users_url)
        todo_response = requests.get(todo_url)
        user_response.raise_for_status()
        todo_response.raise_for_status()
        user_data = user_response.json()
        todo_data = todo_response.json()

        employee_name = user_data['name']
        json_data = {str(employee_ID): []}
        
        for task in todo_data:
            json_data[str(employee_ID)].append({
                'task': task['title'],
                'completed': task['completed'],
                'username': employee_name
            })
        
        json_filename = f'{employee_ID}.json'
        
        with open(json_filename, 'w') as file:
            json.dump(json_data, file)

        print(f'Tasks for user {employee_ID} exported to {json_filename}')
    
    except requests.exceptions.RequestException as e:
        print(f'Error occurred: {e}')

