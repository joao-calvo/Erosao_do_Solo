import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import frases_resposta as rf

meses = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']


def create_window(perda_max):
    fig, ax = plt.subplots()
    ax.bar(meses, perda_max, color='blue')
    ax.set_xlabel('Meses')
    ax.set_ylabel('Perda Máxima de solo em Mg.ha-1')
    ax.set_title('Perda Máxima de solo')

    layout = [[sg.Canvas(key='-CANVAS-')],
              [sg.Button('Fechar')]]

    window = sg.Window('Gráfico com PySimpleGUI', layout, finalize=True)
    canvas_elem = window['-CANVAS-']
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

    layout = [[sg.Canvas(key='-CANVAS-')],
              [sg.Button('Fechar')]]

    window = sg.Window('Gráfico com PySimpleGUI', layout, finalize=True)
    canvas_elem = window['-CANVAS-']
    canvas = FigureCanvasTkAgg(fig, master=canvas_elem.Widget)
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Fechar'):
            break

    window.close()


def create_window_resultado_geral(perda_total, ambiente_producao, tolerancia_perda):
    if ambiente_producao == 'Grupo 1':
        layout = [[sg.Text(rf.Grupo_1)],
                  [sg.Text(
                      f'Perda de solo anual de {perda_total} Mg.ha-1, seu solo tolera perdas de {tolerancia_perda} Mg'
                      f'.ha-1 ')]]
    if ambiente_producao == 'Grupo 2':
        layout = [[sg.Text(rf.Grupo_2)],
                  [sg.Text(
                      f'Perda de solo anual de {perda_total} Mg.ha-1, seu solo tolera perdas de {tolerancia_perda} Mg'
                      f'.ha-1 ')]]
    if ambiente_producao == 'Grupo 3':
        layout = [[sg.Text(rf.Grupo_3)],
                  [sg.Text(
                      f'Perda de solo anual de {perda_total} Mg.ha-1, seu solo tolera perdas de {tolerancia_perda} Mg'
                      f'.ha-1 ')]]
    if ambiente_producao == 'Grupo 4':
        layout = [[sg.Text(rf.Grupo_4)],
                  [sg.Text(
                      f'Perda de solo anual de {perda_total} Mg.ha-1, seu solo tolera perdas de {tolerancia_perda} Mg.ha-1 ')]]
    if ambiente_producao == 'Grupo 5':
        layout = [[sg.Text(rf.Grupo_5)],
                  [sg.Text(
                      f'Perda de solo anual de {perda_total} Mg.ha-1, seu solo tolera perdas de {tolerancia_perda} Mg.ha-1')]]

    window = sg.Window('Gráfico com PySimpleGUI', layout, finalize=True)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Fechar'):
            break

    window.close()
