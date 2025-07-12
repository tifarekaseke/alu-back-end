#!/usr/bin/python3
"""
This script retrieves the TODO list progress of a specific employee
from JSONPlaceholder based on the provided employee ID.
"""

import requests
import sys


def get_employee_progress(employee_id):

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    user_response = requests.get(user_url)
    if user_response.status_code == 200:
        employee_name = user_response.json().get("name")
    else:
        print(f"Employee with ID {employee_id} not found.")

    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    completed_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks"
          f"({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer for employee ID.")
        sys.exit(1)
