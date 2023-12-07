import chuva as ch
import PySimpleGUI as sg

meses = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
valores_r = []
valores_r_modelo = {}




def create_window():
    valores_r.clear()
    lista_chuva = []
    lista_chuva_modelo = {}

    medias_mensais = {}

    sg.theme('DarkBrown6')

    layout = [[sg.Text('Ano: ')], [sg.InputText(key='ano', text_color='white'), ],
              [sg.Text('Estado')], [sg.InputText(key='estado', text_color='white')],
              [sg.Button('Calcular', key='calcular')],
              [sg.Button('Calcular modelo',key='modelo'),sg.Text('Para calcular o modelo insira apenas o Estado')]
              ]


    window = sg.Window('EROMIT', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == 'calcular':
            media_anual = (ch.calcular_medias_anual(int(values['ano'])))
            for mes in meses:
                lista_chuva.append(ch.calcular_media_mensal(int(values['ano']), mes))
            for dado in lista_chuva:
                valores_r.append(ch.erosividade(values['estado'], media_anual, dado))
            print(valores_r)
            window.close()

        if event == 'modelo':
            for ano in range(1917, 2023):
                lista_chuva_modelo[str(ano)] = ch.calcular_medias_anual(ano)
                listinha = []
                for mes in meses:
                    listinha.append(ch.calcular_media_mensal(ano, mes))
                medias_mensais[str(ano)] = listinha
            print(medias_mensais)
            print(len(medias_mensais))

            import copy

            for dado in medias_mensais.keys():
                i = 1

                valores_r_modelo[dado] = {}

                for media in medias_mensais[dado]:
                    dicionario_padrao = {}
                    valor_erosividade = ch.erosividade(values['estado'], lista_chuva_modelo[dado], media)
                    if i == 1:
                        dicionario_padrao['JAN'] = copy.deepcopy(valor_erosividade)
                        valores_r_modelo[dado]['JAN'] = dicionario_padrao['JAN']
                    elif i == 2:
                        dicionario_padrao['FEV'] = copy.deepcopy(valor_erosividade)
                        valores_r_modelo[dado]['FEV'] = dicionario_padrao['FEV']
                    elif i == 3:
                        dicionario_padrao['MAR'] = copy.deepcopy(valor_erosividade)
                        valores_r_modelo[dado]['MAR'] = dicionario_padrao['MAR']
                    elif i == 4:
                        dicionario_padrao['ABR'] = copy.deepcopy(valor_erosividade)
                        valores_r_modelo[dado]['ABR'] = dicionario_padrao['ABR']
                    elif i == 5:
                        dicionario_padrao['MAI'] = copy.deepcopy(valor_erosividade)
                        valores_r_modelo[dado]['MAI'] = dicionario_padrao['MAI']
                    elif i == 6:
                        dicionario_padrao['JUN'] = copy.deepcopy(valor_erosividade)
                        valores_r_modelo[dado]['JUN'] = dicionario_padrao['JUN']
                    elif i == 7:
                        dicionario_padrao['JUL'] = copy.deepcopy(valor_erosividade)
                        valores_r_modelo[dado]['JUL'] = dicionario_padrao['JUL']
                    elif i == 8:
                        dicionario_padrao['AGO'] = copy.deepcopy(valor_erosividade)
                        valores_r_modelo[dado]['AGO'] = dicionario_padrao['AGO']
                    elif i == 9:
                        dicionario_padrao['SET'] = copy.deepcopy(valor_erosividade)
                        valores_r_modelo[dado]['SET'] = dicionario_padrao['SET']
                    elif i == 10:
                        dicionario_padrao['OUT'] = copy.deepcopy(valor_erosividade)
                        valores_r_modelo[dado]['OUT'] = dicionario_padrao['OUT']
                    elif i == 11:
                        dicionario_padrao['NOV'] = copy.deepcopy(valor_erosividade)
                        valores_r_modelo[dado]['NOV'] = dicionario_padrao['NOV']
                    elif i == 12:
                        dicionario_padrao['DEZ'] = copy.deepcopy(valor_erosividade)
                        valores_r_modelo[dado]['DEZ'] = dicionario_padrao['DEZ']

                    i += 1
            print(valores_r_modelo)
            window.close()

    window.close()
