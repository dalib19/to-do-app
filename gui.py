import functions as func
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
add_list = sg.Listbox(values=func.get_todos(), key="todos_list", size=[45, 10], enable_events=True)

left_column_content = [[add_list]]
right_column_content = [[edit_button],
                        [complete_button]]

left_column = sg.Column(left_column_content)
right_column = sg.Column(right_column_content)

window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [left_column, right_column],
                           [exit_button]],
                   font=("Arial", 18))

while True:
    event, values = window.read()

    match event:
        case "Add":
            todos = func.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            func.write_todos(todos)
            window["todos_list"].update(values=todos)
        case "Edit":
            edit_input = values["todo"]
            to_edit = values["todos_list"][0]

            todos = func.get_todos()
            index = todos.index(to_edit)
            todos[index] = edit_input
            func.write_todos(todos)
            window["todos_list"].update(values=todos)
        case "Complete":
            to_complete = values["todos_list"][0]

            todos = func.get_todos()
            index = todos.index(to_complete)
            todos.pop(index)
            func.write_todos(todos)
            window["todos_list"].update(values=todos)
            window["todo"].update(value="")
        case "Exit":
            exit()
        case "todos_list":
            window['todo'].update(value=values['todos_list'][0])
        case sg.WIN_CLOSED:
            break

window.close()
