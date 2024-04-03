from pymongo import MongoClient
from bson.objectid import ObjectId

class TaskManager:
    def __init__(self, host='localhost', port=27017, db_name='task_manager', collection_name='tasks'):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create_task(self, title, description, status='Pending'):
        task = {
            'title': title,
            'description': description,
            'status': status
        }
        result = self.collection.insert_one(task)
        return result.inserted_id

    def get_all_tasks(self):
        return list(self.collection.find())

    def update_task_status(self, task_id, new_status):
        result = self.collection.update_one({'_id': ObjectId(task_id)}, {'$set': {'status': new_status}})
        return result.modified_count

    def delete_task(self, task_id):
        result = self.collection.delete_one({'_id': ObjectId(task_id)})
        return result.deleted_count

def print_tasks(tasks):
    for task in tasks:
        print(f"ID: {task['_id']}, Title: {task['title']}, Description: {task['description']}, Status: {task['status']}")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update task status")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.create_task(title, description)
            print("Task added successfully.")

        elif choice == '2':
            tasks = task_manager.get_all_tasks()
            print("All Tasks:")
            print_tasks(tasks)

        elif choice == '3':
            task_id = input("Enter task ID: ")
            new_status = input("Enter new status (e.g., Completed, In Progress, Pending): ")
            if task_manager.update_task_status(task_id, new_status):
                print("Task status updated successfully.")
            else:
                print("Task not found.")

        elif choice == '4':
            task_id = input("Enter task ID to delete: ")
            if task_manager.delete_task(task_id):
                print("Task deleted successfully.")
            else:
                print("Task not found.")

        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
