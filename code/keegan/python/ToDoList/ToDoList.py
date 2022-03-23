'''
Each To Do Item will have three properties:
- id: integer
- title: string
- completed: boolean
'''
import json

class ToDoItem:
    def __init__(self, title, todo_id, completed = False):
        self.id = todo_id
        self.title = title
        self.completed = completed

    def __str__(self):
        '''1. Walk the dog - completed: False'''
        return f"{self.id}. {self.title} - Completed: {self.completed}"



class ToDoList:
    def __init__(self):
        self.todos = []

        # id_count will be the unique identifier for each ToDoItem object
        self.id_count = 1

        # name of the file from which to load and to which to save todos
        self.storage_file = 'todos.json'

    def add(self, title):
        '''Add a new ToDoItem to the end of the list'''
        # instantiate a new ToDoItem object
        new_todo = ToDoItem(title=title, todo_id=self.id_count)

        # add the new_todo to the end of the ToDoList
        self.todos.append(new_todo)

        self.id_count += 1

    def complete(self, target_id):
        for todo in self.todos:
            # if the current todo is the ToDoItem with the target id
            if todo.id == target_id:
                # set the target todo item's completed attribute to True
                todo.completed = True


    def load(self):
        '''Read the JSON file and pull the todos into the code'''
        
        with open(self.storage_file, 'r') as json_file:
            data = json_file.read()

            # json.loads() is the opposite of json.dumps()
            todos = json.loads(data)

        for todo in todos:
            new_todo = ToDoItem(
                title=todo['title'],
                todo_id=todo['id'],
                completed=todo['completed']
            )

            self.todos.append(new_todo)
        
        # update the id_count to the current length of the loaded todos list
        self.id_count = len(self.todos)


    def save(self):
        '''Write the current list of todo items to a JSON file for storage'''
        # create a context manager inside which the json file is open
        
        todo_data = []

        # Convert each item to a dictionary containing its data
        for todo in self.todos:
            todo_item = {
                'id': todo.id,
                'title': todo.title,
                'completed': todo.completed
            }
            todo_data.append(todo_item)

        # open a json file for writing
        with open(self.storage_file, 'w') as json_file:
            # convert the Python list of dicts
            # into a json string
            todo_data = json.dumps(todo_data, indent=2)

            # write the final json string to the file
            json_file.write(todo_data)
    
    def __str__(self):
        # if the list is empty, say so
        if len(self.todos) == 0:
            return 'Nothing to do...'
        else:
            # return all the todo items with a new line between each
            return "\n".join([str(todo) for todo in self.todos]) + '\n'



# todo_1 = ToDoItem('Walk the dog', 1)
# todo_2 = ToDoItem('Plant onions', 2)
# print(todo_1) # 1. Walk the dog - Completed: False
# print(todo_1.title) # Walk the dog
# print(todo_1.completed) # False


todo_list = ToDoList()
# print(todo_list)

# todo_list.add('Walk the dog')
# todo_list.add('Plant onions')
# todo_list.add('Water the garden')
# print(todo_list)

# todo_list.complete(2)
# todo_list.complete(3)
# print(todo_list)

# todo_list.save()
todo_list.load()
print(todo_list)