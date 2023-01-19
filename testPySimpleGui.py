import PySimpleGUI as sg


sg.theme("LightPurple")

layout = [

    [sg.Text("Hello World")]
]

window = sg.Window( title = "FirstTest", layout = layout, margins = (100,50)).read()