import os

todo_list = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def view_tasks():
    if not todo_list:
        print("There is no tasks in the list.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def remove_task(task_number):
    try:
        task = todo_list.pop(task_number - 1)
        print(f"Task '{task}' removed from the list.")
    except IndexError:
        print("Invalid task number.")

def update_task(task_number, new_task):
    try:
        todo_list[task_number - 1] = new_task
        print(f"Task {task_number} updated to '{new_task}'.")
    except IndexError:
        print("Invalid task number.")

def show_menu():
    print("\nTo-Do List Application")
    print("\n1. Create a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Update a task")
    print("5. Exit")

def main():
    while True:
        clear_screen()
        show_menu()
        choice = input("\nChoose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
            input("\nPress Enter to continue to create your task")
        elif choice == '3':
            view_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
            input("\nPress Enter to continue to create your task")
        elif choice == '4':
            view_tasks()
            try:
                task_number = int(input("Enter the task number to update: "))
                new_task = input("Enter the new task: ")
                update_task(task_number, new_task)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
            input("\nPress Enter to continue to create your task")
        elif choice == '5':
            print("To Do List Created")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            input("\nPress Enter to continue to create your task")

if __name__ == "__main__":
    main()
