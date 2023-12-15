import functions
import PySimpleGUI as py
import time

py.theme("DarkTeal4")

clock = py.Text(' ', key='clock')
label = py.Text("Type in a to-do")
input_box = py.InputText(tooltip="Enter to-do", key="todo")
add_button = py.Button(size=10, image_source="add.png", mouseover_colors="LightBlue2",
                       tooltip="Add Todo", key="Add")
# noinspection PyTypeChecker
list_box = py.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = py.Button("Edit")
complete_button = py.Button(size=10, image_source="complete.png", mouseover_colors="LightBlue2",
                            tooltip="Complete Todo", key="Complete")
exit_button = py.Button("Exit")

button_labels = ["Close", "Apply"]

window = py.Window('My TO-DO App',
                   layout=[[clock],
                           [label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 10))
while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                py.popup("Please select an item first. ", font=('Helvetica', 10))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                py.popup("Please select an item first. ", font=('Helvetica', 10))

        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'])

        case py.WIN_CLOSED:
            break

print("Bye")
window.close()
