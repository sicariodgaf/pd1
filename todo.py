class InvalidArgumentError(Exception):
    pass


class InvalidStatusError(Exception):
    pass


class TodoList:
    def __init__(self):
        self.tasks = {}
        self.current_id = 1
        self.valid_statuses = {'todo', 'inProgress', 'done'}

    def add_task(self, description, status='todo'):
        if not isinstance(description, str) or not description:
            raise InvalidArgumentError("INVALID_ARGUMENT")
        if status and status not in self.valid_statuses:
            raise InvalidStatusError("INVALID_STATUS")

        self.tasks[self.current_id] = {'description': description, 'status': status}
        self.current_id += 1

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def change_status(self, task_id, status):
        if task_id not in self.tasks:
            return False
        if status not in self.valid_statuses:
            raise InvalidStatusError("INVALID_STATUS")

        if self.tasks[task_id]['status'] == status:
            return False

        self.tasks[task_id]['status'] = status
        return True

    def show_list(self):
        todo_list = []
        in_progress_list = []
        done_list = []

        for task_id, task in self.tasks.items():
            if task['status'] == 'todo':
                todo_list.append(f'{task_id} "{task["description"]}"')
            elif task['status'] == 'inProgress':
                in_progress_list.append(f'{task_id} "{task["description"]}"')
            elif task['status'] == 'done':
                done_list.append(f'{task_id} "{task["description"]}"')

        print("Todo:")
        print(",\n  ".join(todo_list) if todo_list else "-")
        print("In Progress:")
        print(",\n  ".join(in_progress_list) if in_progress_list else "-")
        print("Done:")
        print(",\n  ".join(done_list) if done_list else "-")


todo_list = TodoList()

todo_list.add_task('create a task')
todo_list.add_task('eat', 'todo')
todo_list.add_task('sleep', 'inProgress')

todo_list.change_status(1, 'inProgress')
todo_list.change_status(2, 'done')

todo_list.delete_task(1)

todo_list.show_list()
