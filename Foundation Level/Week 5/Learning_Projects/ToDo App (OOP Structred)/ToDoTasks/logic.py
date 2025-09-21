from . import storage
from .models import Task

class TaskManager:
    def __init__(self):
        """
        عند إنشاء المدير، يقوم بتحميل المهام المحفوظة تلقائيًا.
        """
        self._tasks = storage.load_tasks()

    def get_tasks(self):
        """
        تُرجع قائمة المهام الحالية.
        """
        return self._tasks

    def add_task(self, title):
        """
        تضيف مهمة جديدة إلى القائمة.
        """
        # التحقق من عدم تكرار المهمة
        for task in self._tasks:
            if task.title.lower() == title.lower():
                print(f"Task '{title}' already exists.")
                return

        # إنشاء هوية فريدة جديدة
        new_id = len(self._tasks)
        new_task = Task(id=new_id, title=title)
        self._tasks.append(new_task)
        storage.save_tasks(self._tasks)
        print("Task added successfully!")

    def mark_task_complete(self, task_id):
        """
        تحدد مهمة كما تم إنجازها بناءً على رقمها.
        """
        if 0 <= task_id < len(self._tasks):
            task = self._tasks[task_id]
            task.completed = True
            storage.save_tasks(self._tasks)
            print(f"Task '{task.title}' marked as complete. ✔")
        else:
            print("Invalid task number.")

    def delete_task(self, task_id):
        """
        تحذف مهمة بناءً على رقمها.
        """
        if 0 <= task_id < len(self._tasks):
            removed_task = self._tasks.pop(task_id)
            # تحديث الـ IDs للمهام المتبقية
            for i, task in enumerate(self._tasks):
                task.id = i
            storage.save_tasks(self._tasks)
            print(f"Task '{removed_task.title}' deleted successfully.")
        else:
            print("Invalid task number.")

    def export_tasks(self):
        """
        تطلب من مسؤول الأرشيف تصدير المهام.
        """
        storage.export_to_csv(self._tasks)