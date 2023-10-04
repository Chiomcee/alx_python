#!/usr/bin/python3

import csv
import sys
import requests

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
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for task in todos_data:
            task_completed = task['completed']
            task_title = task['title']
            writer.writerow([employee_id, employee_username, task_completed, task_title])

    print(f"Data exported to {filename} successfully.")

def count_completed_tasks(employee_id):
    filename = f"{employee_id}.csv"

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            completed_tasks = sum(1 for row in csv_reader if row['TASK_COMPLETED_STATUS'] == 'True')
            print(f"Number of tasks in CSV: {completed_tasks}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")

def get_user_info(employee_id):
    filename = f"{employee_id}.csv"

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            for row in csv_reader:
                user_id = row[0]
                username = row[1]
                if int(user_id) == employee_id:
                    print(f"User ID: {user_id}")
                    print(f"Username: {username}")
                    break
            else:
                print(f"User not found with ID: {employee_id}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")

# Entry point of the program
if __name__ == "__main__":
    if len(sys.argv) >= 3:
        action = sys.argv[1]
        employee_id = int(sys.argv[2])

        if action == 'export':
            export_employee_todo_list_csv(employee_id)
        elif action == 'count':
            count_completed_tasks(employee_id)
        elif action == 'info':
            get_user_info(employee_id)
        else:
            print("Invalid action. Please choose 'export', 'count', or 'info'.")
    else:
        print("Invalid arguments. Please provide an action (export, count, info) and an employee ID.")