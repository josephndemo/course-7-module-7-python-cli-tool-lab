class Task:
    def __init__(self, title):
        if not title.strip():
            raise ValueError("Task title cannot be empty.")
        self.title = title
        self.completed = False

    def complete(self):
        if self.completed:
            print(f"⚠️ Task '{self.title}' is already completed.")
        else:
            self.completed = True
            print(f"✅ Task '{self.title}' completed.")

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.title}"


class User:
    def __init__(self, name):
        if not name.strip():
            raise ValueError("User name cannot be empty.")
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def list_tasks(self):
        if not self.tasks:
            print("📭 No tasks found.")
            return

        print(f"\n📝 Tasks for {self.name}:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def find_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None