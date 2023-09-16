import function
import PySimpleGUI as sg

label = sg.Text("Type Your To-Do")
input_box = sg.InputText(tooltip="Enter Your To-Do")
add_button = sg.Button("Add")
window = sg.Window('''Akshit's To-Do App''', layout=[[label], [input_box, add_button]])
window.read()
window.close()
