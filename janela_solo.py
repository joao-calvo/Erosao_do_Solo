import PySimpleGUI as sg

import janela_chuva as jch
import manejo_conservacionista as mc
import solo as sl

perda_max = []


def create_window():
    sg.theme('LightBlue')

    solo = {}

    layout = [
        [sg.Text('Classe do solo'), sg.InputText(key='classe')],
        [sg.Text('Teor de argila'), sg.InputText(key='argila')],
        [sg.Text('Classe de silte'), sg.InputText(key='silte')],
        [sg.Text('Classe de areia'), sg.InputText(key='areia')],
        [sg.Text('Declividade'), sg.InputText(key='declividade')],
        [sg.Text('Cultivo: ')],
        [sg.Checkbox(nome, key=nome) for nome in mc.cultivo.keys()],
        [sg.Text('Preparo: ')],
        [sg.Checkbox(nome, key=nome) for nome in mc.preparo.keys()],
        [sg.Text('Pratica: ')],
        [sg.Checkbox(nome, key=nome) for nome in mc.pratica.keys()],
        [sg.Button('Inserir')]
    ]

    window = sg.Window('Erosão do solo', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Inserir':
            valor_k = sl.boyoccos(int(values['argila']), int(values['silte']), int(values['areia']))
            for x in values.keys():
                if not values[x]:
                    continue
                else:
                    solo[x] = values[x]
            print(solo)
            *resto, cultivo, preparo, pratica = solo.keys()
            declividade = float(values['declividade'])

            print(cultivo, preparo, pratica)

            if cultivo in mc.cultivo.keys():
                cultivo = mc.cultivo[cultivo]
            if preparo in mc.preparo.keys():
                preparo = mc.preparo[preparo]
            if pratica in mc.pratica.keys():
                pratica = mc.pratica[pratica]

            for r in jch.valores_r:
                perda_max.append(sl.max_perda_solo(valor_k, r, declividade, cultivo, preparo, pratica))
            if not perda_max:
                print('Você precisa calcular a chuva antes')
            else:
                print(perda_max)
                window.close()

    window.close()
