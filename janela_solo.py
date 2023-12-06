import PySimpleGUI as sg
import solo as sl
import manejo_conservacionista as mc
import chuva as ch

def create_window():
    sg.theme('DarkAmber')

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
                if values[x] == False:
                    continue
                else:
                    solo[x] = values[x]
            *resto, cultivo, preparo, pratica = solo.keys()
            declividade = float(values['declividade'])


            if cultivo in mc.cultivo.keys():
                cultivo = mc.cultivo[cultivo]
            if preparo in mc.preparo.keys():
                preparo = mc.preparo[preparo]
            if pratica in mc.pratica.keys():
                pratica = mc.pratica[pratica]

            medias = ch.x
            valor_r = ch.erosividade('SP',medias[0],medias[1])


            perda_max = sl.max_perda_solo(valor_k,valor_r,declividade,cultivo,preparo,pratica)
            print(perda_max)





    window.close()
