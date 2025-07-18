# todo.py - Simple CLI To-Do App

tasks_file = "tasks.txt"

# Load existing tasks
def load_tasks():
    try:
        with open(tasks_file, "r") as f:
            return [task.strip() for task in f.readlines()]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(tasks_file, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Show all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Your Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Add new task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

# Remove task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        print("\nOptions: view | add | remove | exit")
        choice = input("Choose action: ").strip().lower()

        if choice == "view":
            view_tasks(tasks)
        elif choice == "add":
            add_task(tasks)
        elif choice == "remove":
            remove_task(tasks)
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
