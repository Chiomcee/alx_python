#!/usr/bin/python3

import csv
import requests
import sys

def export_employee_todo_list_csv(employee_id):
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Retrieve employee details
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_username = employee_data['username']
    employee_name = employee_data['name']

    # Retrieve TODO list for the employee
    response = requests.get(todos_url)
    todos_data = response.json()

    filename = f"{employee_id}.csv"

    # Retrieve relevant fields for each task and write to CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for task in todos_data:
            task_completed = task['completed']
            task_title = task['title']
            writer.writerow([employee_id, employee_username, task_completed, task_title])

    print(f"Data exported to {filename} successfully.")

# Entry point of the program
if __name__ == "__main__":
    if len(sys.argv) == 2:
        employee_id = int(sys.argv[1])
        export_employee_todo_list_csv(employee_id)
    else:
        print("Invalid argument. Please provide an employee ID.")