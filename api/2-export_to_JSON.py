#!/usr/bin/python3

#!/usr/bin/python3

import json
import sys
import requests

def get_employee_todo_list(employee_id):
    # defines a function that takes an `employee_id` as an input
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
    completed_tasks = [{"task": task['title'], "completed": task['completed'], "username": employee_name} for task in todos_data]

    # Create JSON file
    filename = f"{employee_id}.json"
    with open(filename, mode='w') as file:
        json.dump({str(employee_id): completed_tasks}, file)

    print(f"Data exported to {filename} successfully.")

# Entry point of the program
if __name__ == "__main__":
    if len(sys.argv) == 2:
        employee_id = int(sys.argv[1])
        get_employee_todo_list(employee_id)
    else:
        print("Invalid argument. Please provide an employee ID.")
