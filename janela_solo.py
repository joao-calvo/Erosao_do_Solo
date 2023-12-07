import PySimpleGUI as sg

import janela_chuva as jch
import manejo_conservacionista as mc
import solo as sl
import resultado as rs

perda_max = []
perda_max_modelo = {}
meses = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']


def create_window():
    sg.theme('DarkBrown6')

    solo = {}

    layout = [
        [sg.Text('Classe do solo'), sg.InputText(key='classe', text_color='white')],
        [sg.Text('Teor de argila'), sg.InputText(key='argila', text_color='white')],
        [sg.Text('Classe de silte'), sg.InputText(key='silte', text_color='white')],
        [sg.Text('Classe de areia'), sg.InputText(key='areia', text_color='white')],
        [sg.Text('Declividade'), sg.InputText(key='declividade', text_color='white')],
        [sg.Text('Cultivo: ')],
        [sg.Checkbox(nome, key=nome) for nome in mc.cultivo.keys()],
        [sg.Text('Preparo: ')],
        [sg.Checkbox(nome, key=nome) for nome in mc.preparo.keys()],
        [sg.Text('Pratica: ')],
        [sg.Checkbox(nome, key=nome) for nome in mc.pratica.keys()],
        [sg.Button('Inserir')],
        [sg.Button('Inserir modelo', key='modelo')]
    ]

    window = sg.Window('EROMIT', layout)

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

            if solo['classe'] == 'Latossolo':
                declividade = (declividade ** 1.18) * 0.00984 * (200 ** 0.63)
            else:
                declividade = (declividade ** 1.18) * 0.00984 * (600 ** 0.63)

            print(f"###{declividade}")

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
                somas = 0
                for i in perda_max:
                    somas += i
                print(f"#####{somas}")

                rs.create_window(perda_max)
                rs.create_window_resultado_geral(somas,sl.ambientes_producao(values['classe'],values['argila']),sl.tolerancia_perda[values['classe']])
                solo.clear()
                perda_max.clear()
                for key in values:
                    if isinstance(window[key], sg.Input):
                        window[key]('')
                    elif isinstance(window[key], sg.Checkbox):
                        window[key](False)
        if event == 'modelo':

            valor_k = sl.boyoccos(int(values['argila']), int(values['silte']), int(values['areia']))
            for x in values.keys():
                if not values[x]:
                    continue
                else:
                    solo[x] = values[x]
            print(solo)
            *resto, cultivo, preparo, pratica = solo.keys()
            declividade = float(values['declividade'])

            if solo['classe'] == 'Latossolo':
                declividade = (declividade ** 1.18) * 0.00984 * (200 ** 0.63)
            else:
                declividade = (declividade ** 1.18) * 0.00984 * (600 ** 0.63)

            print(f"###{declividade}")

            print(cultivo, preparo, pratica)

            if cultivo in mc.cultivo.keys():
                cultivo = mc.cultivo[cultivo]
            if preparo in mc.preparo.keys():
                preparo = mc.preparo[preparo]
            if pratica in mc.pratica.keys():
                pratica = mc.pratica[pratica]

            dic_modelo = {}

            for ano in range(1917, 2023):
                soma = 0
                for mes in meses:
                    perda_max_modelo = sl.max_perda_solo(valor_k, jch.valores_r_modelo[str(ano)][mes], declividade,
                                                         cultivo, preparo, pratica)
                    soma+= perda_max_modelo
                dic_modelo[str(ano)] = soma
            print(dic_modelo)

            lista_teste = []
            for ano in dic_modelo.keys():
                lista_teste.append(dic_modelo[ano])

            rs.create_window_modelo(lista_teste)


    window.close()
