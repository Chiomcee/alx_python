#!/usr/bin/python3


import requests
import sys
import csv

def get_employee_todo_list(employee_id):
    # defines a function called `export_employee_todo_list_csv` that takes an `employee_id` as an input
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
    completed_tasks = [task for task in todos_data if task['completed']]

    # Create CSV file
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in completed_tasks:
            writer.writerow([employee_id, employee_name, str(task['completed']), task['title']])

    print(f"Data exported to {filename} successfully.")
# Entry point of the program
if __name__ == "__main__":
    if len(sys.argv) == 2:
        employee_id = int(sys.argv[1])
        get_employee_todo_list(employee_id)
    else:
        print("Invalid argument. Please provide an employee ID.")