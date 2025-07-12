#!/usr/bin/python3
"""
Fetches tasks from all employees from JSONPlaceholder
and exports them to a single JSON file in the specified format
"""

import json
import requests

if __name__ == "__main__":
    # Get all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users = users_response.json()

    # Prepare dictionary to store everything
    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Get user's taks
        todos_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        )
        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        # List of formatteed task
        task_list = []
        for task in todos:
            task_list.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        # Add to main dictionary
        all_tasks[str(user_id)] = task_list

    # Export to JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
