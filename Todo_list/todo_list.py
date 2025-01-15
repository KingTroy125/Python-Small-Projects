# Todo List Application

# List to store tasks
todo_list = []

# Function to add task
def add_task(task):
    todo_list.append(task)
    print(f'Task "{task}" added to the list.')

# Function to view tasks
def view_tasks():
    if len(todo_list) == 0:
        print("Your todo list is empty!")
    else:
        print("Your Todo List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

# Function to delete task
def delete_task(task_number):
    if 0 < task_number <= len(todo_list):
        removed = todo_list.pop(task_number - 1)
        print(f'Task "{removed}" has been removed.')
    else:
        print("Invalid task number!")

# Main loop
def main():
    while True:
        print("\nOptions: [1] Add task [2] View tasks [3] Delete task [4] Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the application
if __name__ == "__main__":
    main()
