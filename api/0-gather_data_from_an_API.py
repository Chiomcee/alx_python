#!/usr/bin/python3
"""
    Python script that, using this REST API, for a given employee ID
"""

import requests
import sys

def get_employee_todo_list(employee_id):
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Retrieve employee details
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data['name']

    # Retrieve TODO list for the employee
    response = requests.get(todos_url)
    todos_data = response.json()

    # Filter completed tasks
    completed_tasks = [task['title'] for task in todos_data if task['completed']]

    # Display the progress
    total_tasks = len(todos_data)
    done_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print("\t", task)

# Entry point of the program
if __name__ == "__main__":
    if len(sys.argv) == 2:
        employee_id = int(sys.argv[1])
        get_employee_todo_list(employee_id)
    else:
        print("Invalid argument. Please provide an employee ID.")



