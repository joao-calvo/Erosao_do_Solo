import PySimpleGUI as sg
import janela_solo as jsl
import janela_chuva as jch
import frases_resposta as fr

sg.theme('DarkBrown6')

horizontal_padding = 420

layout = [
    [sg.Button('Chuva'), sg.Button('Solo', key='solo', disabled=True, disabled_button_color='red')],
    [sg.Text(fr.Introducao,font=('Any', 20),pad=((horizontal_padding, 0), (0, 0)))],
    [sg.Text(fr.Introducao_2,font=('Any', 14))],
    [sg.Text(fr.Instrucoes, font=('Any', 14))]
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
