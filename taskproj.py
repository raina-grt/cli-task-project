import json
import sys
import os
from datetime import datetime
datetime.now().strftime("%Y-%m-%d %H:%M")
FILE = "task.json"

def load_json():
    if not os.path.isfile(FILE):
        return []

    with open(FILE, 'r') as f:
        try:
            return json.load(f)
        except json.decoder.JSONDecodeError:

            return []

def save_json(data):
    with open(FILE, 'w') as f:
        json.dump(data, f, indent=4)


def get_new_id(tasks):
    if not tasks:
        return 1
    ids = [task['id'] for task  in tasks]
    return max(ids)+1

def find_task(tasks, id):
    if not tasks:
        return None
    for task in tasks:
        if task['id'] == id:
            return task

STATUS_EMOJI = {
    "todo": "📝",
    "in-progress": "⏳",
    "done": "✅"
}


def show_help():
    help_text = """
CLI Task Manager - Naija Edition

Usage:
    python taskproj.py <command> [options]

Commands:
    add "Task title"                  Add a new task
    list                              Show all tasks
    list todo                         Show only todo tasks
    list in-progress                  Show only in-progress tasks
    list done                         Show only completed tasks

    update <id>                       Update a task
    delete <id>                       Delete a task

    todo <id>                         Mark task as todo
    in-progress <id>                  Mark task as in-progress
    done <id>                         Mark task as done

    --help  or  -h                    Show this help message

Examples:
    python taskproj.py add "Buy data make I code"
    python taskproj.py list done
    python taskproj.py done 3
    python taskproj.py --help
    """
    print(help_text)
def add_task(title):

    now = datetime.now()
    created_at = now.strftime("%Y-%m-%d %H:%M")

    status = ""
    while status not in ["todo", "in-progress", "done"]:
        status = input("Task status (todo/in-progress/done):").strip().lower()


    priority = ""
    while priority not in ["low", "medium", "high"]:
        priority = input("Task priority (low/medium/high): ").strip().lower()
        Description = (input("Task Description:")).strip()


    tasks = load_json()
    new_id = get_new_id(tasks)
    new_task = {
        'id': new_id,
        'title': title,
        'status': status,
        'created_at': now.strftime("%Y-%m-%d %H:%M"),
        'priority': priority,
        "Description": Description,
    }
    tasks.append(new_task)
    save_json(tasks)


    print("\n✅ Task added successfully!")
    print(f"ID: {new_id}")
    print(f"Status: {status} {STATUS_EMOJI[status]}")
    print(f"Priority: {priority}")
    print(f"Title: {title}: {Description}")
    print(f"Created at: {created_at}\n")

def update_task(task_id):

    now = datetime.now()
    updated_at = now.strftime("%Y-%m-%d %H:%M")

    tasks = load_json()
    task = find_task(tasks, task_id)
    if not task:
        print(f"Task {task_id} not found❌")
        return


    new_title = input(f"New title [{task['title']}]: ").strip()
    if not new_title:
        new_title = task["title"]

    Description = (input("Task Description:")).strip()

    new_status = ""
    while new_status not in ["todo", "in-progress", "done"]:
        new_status = input(f"New status (todo/in-progress/done) [{task['status']}]: ").strip().lower()
        if not new_status:
            new_status = task["status"]




    new_priority = ""
    while new_priority not in ["low", "medium", "high"]:
        new_priority = input("Task priority (low/medium/high): ").strip().lower()
        if not new_priority:
            new_priority = task["priority"]

    task['title'] = new_title
    task['status'] = new_status
    task['priority'] = new_priority
    task['Description'] = Description
    task['updated_at']: now.strftime("%Y-%m-%d %H:%M")


    save_json(tasks)

    print("\n✅ Task updated successfully!")
    print(f"ID: {task_id}")
    print(f"Title: {new_title}")
    print(f"Status: {new_status} {STATUS_EMOJI[new_status]}")
    print(f"Priority: {new_priority}")
    print(f"Description: {Description}")
    print(f"updated_at: {updated_at}\n")


def delete_task(task_id):
    tasks = load_json()
    task = find_task(tasks, task_id)
    if  task:
        tasks.remove(task)
        save_json(tasks)
        print(f"Task{task_id} deleted successfully✅")
    else:
        print(f"Task {task_id} not found😪")


def mark_as_in_progress(id):
    tasks = load_json()
    task = find_task(tasks, id)

    if not task:
        print(f"Task {id} not found❌")
        return


    task['status'] = "in-progress"
    save_json(tasks)
    print(f"{task} marked as in_progress⏳😊")

def mark_as_done(id):
    tasks = load_json()
    task = find_task(tasks, id)
    if not task:
        print(f"Task {id} not found❌")
        return

    task['status'] = "done"
    save_json(tasks)
    print(f"{id} marked as done😅✅")

def mark_as_todo(id):
    tasks = load_json()
    task = find_task(tasks, id)
    if not task:
        print(f"Task {id} not found")
        return
    task["status"] = "todo"
    save_json(tasks)
    print(f"{id} marked as todo 📝")

def list_tasks():
    tasks = load_json()

    status_emoji ={
        "todo": "📝",
        "in-progress": "⏳",
        "done": "✅"

    }
    for task in tasks:
       emoji = status_emoji.get(task["status"], "❔")
       print(f"{task['id']}: {task['title']} [{task['status']}] {emoji}")

def list_by_status(status):
    tasks = load_json()

    found = False
    for task in tasks:
        if task["status"] == status:
           print(f"{task['id']}: {task['title']} [{task['status']}]")
           found = True

    if not found:
       print(f"No task found with status: {status}")


if len(sys.argv) == 1 or sys.argv[1] in ["--help", "-h", "-help"]:
    show_help()
    sys.exit()


command = sys.argv[1]
if command == "add":
    if len(sys.argv) < 3:
        print("Usage: add <title>")
        sys.exit()
    add_task(sys.argv[2])

elif command == "update":
    if len(sys.argv) < 3:
        print("Usage: update <id>")
        sys.exit()
    update_task(int(sys.argv[2]))

elif command == "delete":
    delete_task(int(sys.argv[2]))

elif command == "in-progress":
    mark_as_in_progress(int(sys.argv[2]))

elif command == "done":
    mark_as_done(int(sys.argv[2]))

elif command == "todo":
    mark_as_todo(int(sys.argv[2]))

elif command == "list":
    if len(sys.argv) == 2:
        list_tasks()
    else:
        list_by_status(sys.argv[2])
else:
    print("Unknown command")
