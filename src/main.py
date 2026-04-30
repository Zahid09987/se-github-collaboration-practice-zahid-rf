from task_manager import show_tasks, add_tasks, update_status, delete_task, search_by_assignee

def main():
    while True:
        print("\n=== TO-DO LIST PROJECT ===")
        print("1. Show all tasks")
        print("2. Add task")
        print("3. Change task status")
        print("4. Remove task")
        print("5. Search task by assignee")
        print("0. Quit")

        choice = input("Select menu: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_tasks()
        elif choice == "3":
            update_status()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            search_by_assignee()
        elif choice == "0":
            print("This is the end of the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()