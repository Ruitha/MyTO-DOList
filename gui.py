import functions
import PySimpleGUI as py

label = py.Text("Type in a to-do")
input_box = py.InputText(tooltip="Enter to-do", key="todo")
add_button = py.Button("Add")
list_box = py.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = py.Button("Edit")

window = py.Window('My TO-DO App',
                   layout=[[label], [input_box], [add_button],
                           [list_box, edit_button]],
                   font=('Helvetica', 10))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'])

        case py.WIN_CLOSED:
            break

window.close()
