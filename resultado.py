import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import frases_resposta as rf
import janela_solo as jsl
import manejo_conservacionista as mc

meses = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']


def create_window(perda_max):
    fig, ax = plt.subplots()
    ax.bar(meses, perda_max, color='blue')
    ax.set_xlabel('Meses')
    ax.set_ylabel('Perda Máxima de solo em Mg.ha-1')
    ax.set_title('Perda Máxima de solo')

    layout = [[sg.Canvas(key='canva')],
              [sg.Button('Fechar')]]

    window = sg.Window('EROMIT', layout, finalize=True)
    canvas_elem = window['canva']
    canvas = FigureCanvasTkAgg(fig, master=canvas_elem.Widget)
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Fechar'):
            break

    window.close()


def create_window_modelo(perda_max):
    fig, ax = plt.subplots()
    ax.bar(range(1917, 2023), perda_max, color='blue')
    ax.set_xlabel('Anos')
    ax.set_ylabel('Perda Máxima de solo em Mg.ha-1')
    ax.set_title('Perda Máxima de solo')

    layout = [[sg.Canvas(key='canva')],
              [sg.Button('Fechar')]]

    window = sg.Window('EROMIT', layout, finalize=True)
    canvas_elem = window['canva']
    canvas = FigureCanvasTkAgg(fig, master=canvas_elem.Widget)
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Fechar'):
            break

    window.close()


def create_window_resultado_geral(perda_total, ambiente_producao, tolerancia_perda):

    layout = []
    def melhor_resposta(perda_total):
        if perda_total > tolerancia_perda:
            print(perda_total)
            perda_total = perda_total / (jsl.lista_pratica[0])
            print(perda_total)
            melhor_resultado = mc.melhor_resultado(perda_total)

            novo_texto = 'Melhores respostas encontrada:\n'

            for manejo in melhor_resultado.keys():
                novo_texto += f'Plantio de {manejo} - {melhor_resultado[manejo]}\n'

            return novo_texto
        return ''

    resposta = melhor_resposta(perda_total)

    if ambiente_producao == 'Grupo 1':
        layout = [[sg.Text(rf.Grupo_1)],
                  [sg.Text(
                      f'Perda de solo anual de {perda_total} Mg.ha-1, seu solo tolera perdas de {tolerancia_perda} Mg'
                      f'.ha-1. A seguir é mostrado algumas escolhas que estariam dentro das perspectivas de perdas de '
                      f'solo.\n{resposta}', key='resposta')]]
    if ambiente_producao == 'Grupo 2':
        layout = [[sg.Text(rf.Grupo_2)],
                  [sg.Text(
                      f'Perda de solo anual de {perda_total} Mg.ha-1, seu solo tolera perdas de {tolerancia_perda} Mg'
                      f'.ha-1. A seguir é mostrado algumas escolhas que estariam dentro das perspectivas de perdas de '
                      f'solo.\n{resposta}', key='resposta')]]
    if ambiente_producao == 'Grupo 3':
        layout = [[sg.Text(rf.Grupo_3)],
                  [sg.Text(
                      f'Perda de solo anual de {perda_total} Mg.ha-1, seu solo tolera perdas de {tolerancia_perda} Mg'
                      f'.ha-1. A seguir é mostrado algumas escolhas que estariam dentro das perspectivas de perdas de '
                      f'solo.\n{resposta} ', key='resposta')]]
    if ambiente_producao == 'Grupo 4':
        layout = [[sg.Text(rf.Grupo_4)],
                  [sg.Text(
                      f'Perda de solo anual de {perda_total} Mg.ha-1, seu solo tolera perdas de {tolerancia_perda} Mg'
                      f'.ha-1. A seguir é mostrado algumas escolhas que estariam dentro das perspectivas de perdas de '
                      f'solo.\n{resposta} ',
                      key='resposta')]]
    if ambiente_producao == 'Grupo 5':
        layout = [[sg.Text(rf.Grupo_5)],
                  [sg.Text(
                      f'Perda de solo anual de {perda_total} Mg.ha-1, seu solo tolera perdas de {tolerancia_perda} Mg'
                      f'.ha-1. A seguir é mostrado algumas escolhas que estariam dentro das perspectivas de perdas de '
                      f'solo.\n{resposta}',
                      key='resposta')]]

    window = sg.Window('EROMIT', layout, finalize=True)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Fechar'):
            break

    window.close()
