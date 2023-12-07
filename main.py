import PySimpleGUI as sg
import janela_solo as jsl
import janela_chuva as jch

sg.theme('DarkBrown6')

layout = [
    [sg.Button('Chuva'), sg.Button('Solo', key='solo', disabled=True, disabled_button_color='red'),
     sg.Button('Praticas')]
]

window = sg.Window('EROMIT', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Chuva':
        jch.create_window()
        window['solo'].update(disabled=False)
    if event == 'solo':
        jsl.create_window()
    if event == 'Praticas':
        pass

window.close()
