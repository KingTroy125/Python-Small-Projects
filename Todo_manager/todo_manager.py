import json
from datetime import datetime

data_file = "tasks.json"

def load_tasks():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(data_file, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    name = input("Enter task name: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    category = input("Enter category: ").strip()
    try:
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Task not added.\n")
        return

    task = {
        "id": len(tasks) + 1,
        "name": name,
        "due_date": due_date_obj.strftime("%Y-%m-%d"),
        "category": category,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")

def delete_task(tasks):
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid task ID.\n")
        return tasks
    
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Task deleted successfully!\n")
    return tasks

def update_task(tasks):
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Invalid task ID.\n")
        return tasks

    for task in tasks:
        if task["id"] == task_id:
            print(f"Updating task: {task['name']}")
            task["name"] = input("Enter new task name: ").strip() or task["name"]
            new_due_date = input("Enter new due date (YYYY-MM-DD): ").strip()
            if new_due_date:
                try:
                    due_date_obj = datetime.strptime(new_due_date, "%Y-%m-%d")
                    task["due_date"] = due_date_obj.strftime("%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Due date not updated.")
            task["category"] = input("Enter new category: ").strip() or task["category"]
            save_tasks(tasks)
            print("Task updated successfully!\n")
            return tasks
    print("Task not found.\n")
    return tasks

def view_tasks(tasks, filter_by=None):
    if not tasks:
        print("No tasks available.\n")
        return

    if filter_by == "category":
        category = input("Enter category to filter by: ").strip()
        filtered_tasks = [task for task in tasks if task["category"].lower() == category.lower()]
    elif filter_by == "due_date":
        due_date = input("Enter due date to filter by (YYYY-MM-DD): ").strip()
        filtered_tasks = [task for task in tasks if task["due_date"] == due_date]
    else:
        filtered_tasks = tasks

    if not filtered_tasks:
        print("No tasks match the filter criteria.\n")
        return

    for task in filtered_tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f"ID: {task['id']} | Name: {task['name']} | Due: {task['due_date']} | Category: {task['category']} | Status: {status}")
    print()

def mark_complete(tasks):
    try:
        task_id = int(input("Enter task ID to mark as complete: "))
    except ValueError:
        print("Invalid task ID.\n")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("Task marked as complete!\n")
            return
    print("Task not found.\n")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Update Task")
        print("4. View Tasks")
        print("5. View Tasks by Category")
        print("6. View Tasks by Due Date")
        print("7. Mark Task as Complete")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            tasks = delete_task(tasks)
        elif choice == "3":
            tasks = update_task(tasks)
        elif choice == "4":
            view_tasks(tasks)
        elif choice == "5":
            view_tasks(tasks, filter_by="category")
        elif choice == "6":
            view_tasks(tasks, filter_by="due_date")
        elif choice == "7":
            mark_complete(tasks)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
