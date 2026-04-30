import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "tasks.json")

def load_tasks():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks():
    tasks = load_tasks()
    print("\nTasks List:")
    for task in tasks:
        print(f"{task['id']}. {task['title']} | Status: {task['status']} | PIC: {task['assignee']}")

def add_task():
    tasks = load_tasks()

    new_id = max(task["id"] for task in tasks) + 1
    title = input("Task title: ")
    description = input("Description: ")
    priority = input("Priority (High, Medium, Low): ")
    assignee = input("Assignee: ")

    new_task = {
        "id": new_id,
        "title": title,
        "description": description,
        "status": "todo",
        "priority": priority,
        "assignee": assignee
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print("Task added successfully.")

def update_status():
    tasks = load_tasks()

    task_id = int(input("Enter task ID: "))
    new_status = input("New status (todo, in-progress, done): ")

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            save_tasks(tasks)
            print("Task updated successfully.")
            return

    print("Task not found!")

def delete_task():
    tasks = load_tasks()

    task_id = int(input("Enter task ID: "))

    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(new_tasks) == len(tasks):
        print("Task not found.")
    else:
        save_tasks(new_tasks)
        print("Task deleted successfully.")

def search_by_assignee():
    tasks = load_tasks()

    keyword = input("Enter assignee name: ").lower()

    results = [
        task for task in tasks
        if keyword in task["assignee"].lower()
    ]

    if not results:
        print("No tasks found for this assignee.")
    else:
        print("\nSearch Results:")
        for task in results:
            print(f"{task['id']}. {task['title']} | Status: {task['status']} | PIC: {task['assignee']}")