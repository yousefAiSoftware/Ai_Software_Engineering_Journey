from .logic import TaskManager

def menu():
    """Prints the main menu options."""
    print("\n1. Add New Task")
    print("2. View All Tasks")
    print("3. Exit")

def divider():
    """Prints a separator line."""
    print("\n-----------------------\n")

def display_tasks(tasks):
    """Takes a list of Task objects and prints them nicely."""
    if not tasks:
        print("Your ToDo List is Empty.")
        return

    print("----- Your Tasks -----")
    for task in tasks:
        status = "✔" if task.completed else " "
        print(f"{task.id + 1}. {task.title} [{status}]")

def options_menu(manager):
    """Displays task options and calls manager methods."""
    while True:
        print("\n----- Options -----")
        print("1. Mark Task as Completed")
        print("2. Delete Task")
        print("3. Export Tasks to CSV")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                task_num = int(input("Enter the task number to mark as complete: "))
                manager.mark_task_complete(task_num - 1) # Pass index
            except ValueError:
                print("Invalid input. Please enter a number.")
            break
        elif choice == "2":
            try:
                task_num = int(input("Enter the task number to delete: "))
                manager.delete_task(task_num - 1) # Pass index
            except ValueError:
                print("Invalid input. Please enter a number.")
            break
        elif choice == "3":
            manager.export_tasks()
            break
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def start():
    """The main entry point of the application."""
    manager = TaskManager()
    print("Welcome To Our ToDo App (OOP Version)")

    while True:
        divider()
        menu()
        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            task_title = input("Enter the new task title: ")
            manager.add_task(task_title)
        elif user_choice == "2":
            tasks = manager.get_tasks()
            display_tasks(tasks)
            if tasks:
                options_menu(manager)
        elif user_choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select from the menu.")