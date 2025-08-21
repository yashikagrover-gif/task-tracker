tasks = []

def add_task():
    title = input("Enter task title: ")
    priority = input("Enter priority (High/Medium/Low): ").capitalize()
    tasks.append({"title": title, "priority": priority, "status": "Pending"})
    print(f"✅ Task '{title}' added successfully!\n")

def view_tasks():
    if not tasks:
        print("📂 No tasks found!\n")
        return
    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['title']} | Priority: {task['priority']} | Status: {task['status']}")
    print()

def mark_complete():
    view_tasks()
    if not tasks:
        return
    try:
        task_no = int(input("Enter task number to mark complete: "))
        tasks[task_no - 1]['status'] = "Completed"
        print(" Task marked as completed!\n")
    except (IndexError, ValueError):
        print("❌ Invalid task number.\n")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_no = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_no - 1)
        print(f"🗑 Task '{removed['title']}' deleted.\n")
    except (IndexError, ValueError):
        print("❌ Invalid task number.\n")

def main():
    while True:
        print(" Task & Productivity Tracker")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye! Stay productive!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
