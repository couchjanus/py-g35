from todo.model import Todo

class TodoList:

    def __init__(self) -> None:
        self.todo_list = []

    def add(self, todo: Todo):
        """Add a new todo to the database"""

        count = len(self.todo_list)
        todo._position = count if count else 0
        self.todo_list.append(todo)

    def get_todo_list(self):
        """Return todo list"""

        return self.todo_list
    
    def complete(self, position):

        self.todo_list[position-1]._status = 2
    
    