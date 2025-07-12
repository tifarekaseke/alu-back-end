#!/usr/bin/python3
"""
This script retrieves an employee's TODO list from JSONPlaceholder
and exports the data to a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Get employee info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        sys.exit(1)

    employee_username = user_response.json().get("username")

    # Get employee's todos
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Prepare JSON structure
    task_list = []
    for task in todos:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_username
        }
        task_list.append(task_dict)

    json_data = {str(employee_id): task_list}

    # Write to a JSON file
    filename = f"{employee_id}.json"
    with open(filename, "w") as jsonfile:
        json.dump(json_data, jsonfile)
