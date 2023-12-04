import PySimpleGUI as sg
import solo as sl


def create_window():
    sg.theme('DarkAmber')

    layout = [
        [sg.Text('Classe do solo'), sg.InputText(key='classe')],
        [sg.Text('Teor de argila'), sg.InputText(key='argila')],
        [sg.Text('Classe de silte'), sg.InputText(key='silte')],
        [sg.Text('Classe de areia'), sg.InputText(key='areia')],
        [sg.Button('Inserir')]
    ]

    window = sg.Window('Erosão do solo', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Inserir':
            valor_k = sl.boyoccos(int(values['argila']), int(values['silte']), int(values['areia']))
            print(valor_k)

    window.close()
