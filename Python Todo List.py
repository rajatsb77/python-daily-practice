
tasks = []


def show_tasks():
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n===== YOUR TASKS =====")

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['title']}")


def add_task():
    title = input("Enter task: ").strip()

    if not title:
        print("Task cannot be empty.")
        return

    tasks.append({
        "title": title,
        "completed": False
    })

    print("Task added successfully.")


def complete_task():
    show_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to complete: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Deleted: {deleted_task['title']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n===== TODO LIST =====")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()

        elif choice == "2":
            add_task()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
