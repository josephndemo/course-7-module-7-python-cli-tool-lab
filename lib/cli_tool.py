import argparse
from models import Task, User

# In-memory storage
users = {}


def get_or_create_user(username):
    if username not in users:
        users[username] = User(username)
    return users[username]


def add_task(args):
    try:
        user = get_or_create_user(args.user)
        task = Task(args.title)
        user.add_task(task)
    except ValueError as e:
        print(f"❌ Error: {e}")


def list_tasks(args):
    user = users.get(args.user)
    if not user:
        print("❌ User not found.")
        return
    user.list_tasks()


def complete_task(args):
    user = users.get(args.user)
    if not user:
        print("❌ User not found.")
        return

    task = user.find_task(args.title)
    if not task:
        print("❌ Task not found.")
        return

    task.complete()


def main():
    parser = argparse.ArgumentParser(
        description="🗂 Task Manager CLI"
    )

    subparsers = parser.add_subparsers(dest="command")

    # Add Task
    add_parser = subparsers.add_parser("add-task", help="Add a new task")
    add_parser.add_argument("user", help="Username")
    add_parser.add_argument("title", help="Task title")
    add_parser.set_defaults(func=add_task)

    # List Tasks
    list_parser = subparsers.add_parser("list-tasks", help="List all tasks")
    list_parser.add_argument("user", help="Username")
    list_parser.set_defaults(func=list_tasks)

    # Complete Task
    complete_parser = subparsers.add_parser("complete-task", help="Complete a task")
    complete_parser.add_argument("user", help="Username")
    complete_parser.add_argument("title", help="Task title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()