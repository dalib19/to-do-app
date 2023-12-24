FILE_LOCATION = "todos.txt"


def get_todos(filename=FILE_LOCATION):
    with open(filename, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filename=FILE_LOCATION):
    with open(filename, 'w') as file:
        file.writelines(todos_arg)
