import functions
import PySimpleGUI as py

label = py.Text("Type in a to-do")
input_box = py.InputText(tooltip="Enter to-do", key="todo")
add_button = py.Button("Add")

window = py.Window('My TO-DO App',
                   layout=[[label], [input_box], [add_button]],
                   font=('Helvetica', 10))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case"Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case py.WIN_CLOSED:
            break


window.close()

