def get_todos(filename):
    with open(filename, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(filename, todos_arg):
    with open(filename, 'w') as file:
        file.writelines(todos_arg)
