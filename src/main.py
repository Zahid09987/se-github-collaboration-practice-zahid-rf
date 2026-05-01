from utils import _
from task_manager import show_tasks, add_task, update_status, delete_task, search_by_assignee

def main():
    while True:
        print(_("\n=== TO-DO LIST PROJECT ==="))
        print(_("1. Show all tasks"))
        print(_("2. Add task"))
        print(_("3. Change task status"))
        print(_("4. Remove task"))
        print(_("5. Search task by assignee"))
        print(_("0. Quit"))

        choice = input(_("Select menu: "))

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_status()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            search_by_assignee()
        elif choice == "0":
            print(_("This is the end of the program."))
            break
        else:
            print(_("Invalid choice. Please try again."))

if __name__ == "__main__":
    main()