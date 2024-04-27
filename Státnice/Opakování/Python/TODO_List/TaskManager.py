from Task import Task

class TaskManager:
    def __init__(self):
        self._task_list = []
        self._id = 0

    def get_task_list(self):
        return self._task_list
    
    def createTask(self, name, content):
        self._id += 1
        task = Task(self._id, name, content)
        return task

    def createTaskAndAdd(self, name, content):
        self._id += 1
        task = Task(self._id, name, content)
        tasks = self.get_task_list()
        tasks.append(task)

    def addTask(self, task):
        if isinstance(task, Task):
            self.get_task_list().append(task)

    def printTasks(self):
        for task in self.get_task_list():
            print(f"Name: {task.get_name()}\n")
            print(f"Content: {task.get_content()}\n")
            print(f"State:{task.get_active()}\n\n")

    def setTaskAsDone(self, id):
        for task in self.get_task_list():
            if task.get_id() == id:
                task.set_active(False)

    def deleteTask(self, id):
        task_to_delete = None
        for task in self.get_task_list():
            if task.get_id() == id:
                id_to_delete = task
                break
        if (id_to_delete is not None):
            self.get_task_list().remove(task_to_delete)

    def deleteTask(self, task):
        self.get_task_list().remove(task)
