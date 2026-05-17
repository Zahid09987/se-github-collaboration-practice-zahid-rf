def get_all_tasks(tasks):
    return tasks


def add_task(tasks, title, description, priority, assignee):
    new_id = 1 if len(tasks) == 0 else max(task["id"] for task in tasks) + 1
    if title.strip() == "":
        return "Error: Title wajib diisi"

    if priority not in ["low", "medium", "high"]:
        return "Error: Priority tidak valid"
    new_task = {
        "id": new_id,
        "title": title,
        "description": description,
        "status": "todo",
        "priority": priority,
        "assignee": assignee
    }
    tasks.append(new_task)
    return tasks


def update_task_status(tasks, task_id, new_status):

    if new_status not in ["todo", "in_progress", "done"]:
        return "Error: Status tidak valid"

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            return tasks

    return tasks


def delete_task(tasks, task_id):
    return [task for task in tasks if task["id"] != task_id]


def search_task_by_assignee(tasks, keyword):
    return [
        task for task in tasks
        if keyword.lower() in task["assignee"].lower()
    ]

