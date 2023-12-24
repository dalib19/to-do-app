import functions

while True:
    user_action = input("Upisi add/show/edit/complete/exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos("todos.txt")
        todos.append(todo + '\n')
        functions.write_todos('todos.txt', todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos("todos.txt")
        for index, content in enumerate(todos):
            content = content.strip("\n")
            print(f'{index+1}-{content}')

    elif user_action.startswith("edit"):
        index = user_action[5:]
        todos = functions.get_todos("todos.txt")
        print(f"The todo you want to edit is {int(index)}")
        new_todo = input(f"Enter a new todo:")
        todos[int(index)-1] = new_todo + '\n'
        functions.write_todos("todos.txt", todos)

    elif user_action.startswith("complete"):
        index = user_action[9:]
        todos = functions.get_todos('todos.txt')
        todos.pop(index)

    elif user_action.startswith("exit"):
        index = user_action[5:]
        break
