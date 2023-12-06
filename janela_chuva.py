import chuva as ch
import PySimpleGUI as sg

meses = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
valores_r = []


def create_window():
    sg.theme('LightBlue')

    layout = [[sg.Text('Ano: ')], [sg.InputText(key='ano')],
              [sg.Text('Estado')], [sg.InputText(key='estado')],
              [sg.Button('Calcular', key='calcular')]
              ]

    window = sg.Window('Erosão do solo', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == 'calcular':
            x = (ch.calcular_medias_anual(int(values['ano'])))
            lista_chuva = []
            for mes in meses:
                lista_chuva.append(ch.calcular_media_mensal(int(values['ano']), mes))
            for dado in lista_chuva:
                valores_r.append(ch.erosividade(values['estado'], x, dado))
            print(valores_r)
            window.close()

    window.close()
