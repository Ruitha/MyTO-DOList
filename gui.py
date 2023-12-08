import functions
import PySimpleGUI as py

label = py.Text("Type in a to-do")
input_box = py.InputText(tooltip="Enter to-do")
add_button = py.Button("Add")

window = py.Window('My TO-DO App', layout=[[label], [input_box], [add_button]])
window.read()
window.close()
