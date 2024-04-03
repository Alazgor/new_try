import argparse
import json
from datetime import datetime

# Function to load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save tasks to a text file
def save_tasks_to_text(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['name']}|{task['priority']}|{task['deadline']}\n")


# Function to add a task
def add_task(name, priority, deadline):
    tasks.append({"name": name, "priority": priority, "deadline": deadline})
    save_tasks(tasks)
    print("Task added successfully! Here is the current list:")
    display_tasks()

# Function to delete a task
def delete_task(index=None):
    if index is None:
        deleted_task = tasks.pop()
    else:
        deleted_task = tasks.pop(index)
    save_tasks(tasks)
    print("Task deleted successfully! Here is the current list:")
    display_tasks()

# Function to edit a task
def edit_task(old_name, new_name, priority, deadline):
    for task in tasks:
        if task["name"] == old_name:
            task["name"] = new_name
            task["priority"] = priority
            task["deadline"] = deadline
            save_tasks(tasks)
            print("Task edited successfully! Here is the current list:")
            display_tasks()
            return
    print(f'Unfortunately, "{old_name}" task currently does not exist. Try again!')
    display_tasks()

# Function to display tasks
def display_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']}. Due date: {task['deadline']}")

# Parse command line arguments
parser = argparse.ArgumentParser(description='Task Tracking Program')
parser.add_argument('--add', nargs=3, metavar=('name', 'priority', 'deadline'), help='Add a new task')
parser.add_argument('--delete', nargs='?', const=-1, type=int, help='Delete the latest task or specify index to delete')
parser.add_argument('--edit', nargs=4, metavar=('old_name', 'name', 'priority', 'deadline'), help='Edit a task')
args = parser.parse_args()

# Load existing tasks
tasks = load_tasks()

# Perform actions based on arguments
if args.add:
    name, priority, deadline = args.add
    add_task(name, int(priority), deadline)
elif args.delete is not None:
    delete_task(args.delete)
elif args.edit:
    old_name, name, priority, deadline = args.edit
    edit_task(old_name, name, int(priority), deadline)
else:
    print("No valid command provided. Please provide a valid command.")
    parser.print_help()

# how to use the programm - run this in terminal like this:
# python list_of_your_tasks.py --add "Do dishes" --priority 2 --deadline "2024-02-24 12:00"
# python list_of_your_tasks.py --add "Do dishes" 2 "2024-02-24 12:00"
# python list_of_your_tasks.py --add "Do laundry" 1 "2024-02-24 11:00"
# python list_of_your_tasks.py --add "Call grandma" 2 "2024-02-24 15:00"
# python list_of_your_tasks.py --delete 1
# python list_of_your_tasks.py --delete
# python list_of_your_tasks.py --edit "Call grandma" "Call mom" 3 "2024-02-25 17:00"

# text file with list of tasks can find in this directory:
# bash terminal
# cd C:\Users\aleks\CodeAcademy\pythonProject
# Invoke-Item .\tasks.txt
