from utils import _
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
    print(_("\nTasks List:"))
    for task in tasks:
        print(f"{task['id']}. {task['title']} | Status: {task['status']} | PIC: {task['assignee']}")

def add_task():
    tasks = load_tasks()

    new_id = max(task["id"] for task in tasks) + 1

    title = input(_("Task title: ")).strip()
    if not title:
        print(_("Title cannot be empty."))
        return

    description = input(_("Description: ")).strip()

    priority = input(_("Priority (low, medium, high): ")).lower()
    if priority not in ["low", "medium", "high"]:
        print(_("Invalid priority."))
        return

    assignee = input(_("Assignee: ")).strip()
    if not assignee:
        print(_("Assignee cannot be empty."))
        return

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

    print(_("Task added successfully."))

def update_status():
    tasks = load_tasks()

    try:
        task_id = int(input(_("Enter task ID: ")))
    except ValueError:
        print(_("Invalid input. ID must be a number."))
        return

    valid_status = ["todo", "in_progress", "done"]
    new_status = input(_("New status (todo, in_progress, done): ")).lower()

    if new_status not in valid_status:
        print(_("Invalid status."))
        return

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            save_tasks(tasks)
            print(_("Task updated successfully."))
            return

    print(_("Task not found!"))

# improve readability for delete task function
def delete_task():
    tasks = load_tasks()

    try:
        task_id = int(input(_("Enter task ID: ")))
    except ValueError:
        print(_("Invalid input. ID must be a number."))
        return

    for task in tasks:
        if task["id"] == task_id:
            confirm = input(_("Are you sure you want to delete this task? (y/n): ")).lower()

            if confirm == "y":
                tasks.remove(task)
                save_tasks(tasks)
                print(_("Task deleted successfully."))
            else:
                print(_("Deletion cancelled."))
            return

    print(_("Task not found."))

def search_by_assignee():
    tasks = load_tasks()

    keyword = input(_("Enter assignee name: ")).lower()

    results = [
        task for task in tasks
        if keyword in task["assignee"].lower()
    ]

    if not results:
        print(_("No tasks found for this assignee."))
        print("Try Again ?")
        user_input = input(_("Yes/No: ")).lower()
        if user_input == "yes":
            search_by_assignee()
    else:
        print(_("\nSearch Results:"))
        for task in results:
            print(f"{task['id']}. {task['title']} | Status: {task['status']} | PIC: {task['assignee']}")
