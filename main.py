def get_todos(filename):
    with open(filename, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(filename, todos_arg):
    with open(filename, 'w') as file:
        file.writelines(todos_arg)

while True:
    user_action = input("Upisi add/show/edit/complete/exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos("todos.txt")
        todos.append(todo + '\n')
        write_todos('todos.txt', todos)

    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")
        for index, content in enumerate(todos):
            content = content.strip("\n")
            print(f'{index+1}-{content}')

    elif user_action.startswith("edit"):
        index = user_action[5:]
        todos = get_todos("todos.txt")
        print(f"The todo you want to edit is {int(index)}")
        new_todo = input(f"Enter a new todo:")
        todos[int(index)-1] = new_todo + '\n'
        write_todos("todos.txt", todos)

    elif user_action.startswith("complete"):
        index = user_action[9:]
        todos = get_todos('todos.txt')
        todos.pop(index)

    elif user_action.startswith("exit"):
        index = user_action[5:]
        break