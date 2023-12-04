import pandas as pd

def erosividade(regiao, m_anual, m_mensal):
    indice_regiao = ''
    valor_r = ''
    valores_r = {
        '1': ['AM', 'AC', 'RO', 'RR'],
        '2': ['PA', 'MT', 'TO'],
        '3': 'AP',
        '4': '',
        '5': 'Litoral',
        '6': 'MG',
        '7': ['SP', 'MS'],
        '8': ['PR', 'SC', 'RS']
    }

    for chave in valores_r.keys():
        if regiao in valores_r[chave]:
            indice_regiao = int(chave)

    if indice_regiao == 1:
        valor_r = 3.76 * (m_mensal ** 2 / m_anual) + 42, 77
    elif indice_regiao == 2:
        valor_r = 36.849 * ((m_mensal ** 2 / m_anual) ** 1.0852)
    elif indice_regiao == 3:
        valor_r = (0.66 * m_mensal) + 8.88
    elif indice_regiao == 4:
        valor_r = 42.307 * (m_mensal ** 2 / m_anual) + 69.763
    elif indice_regiao == 5:
        valor_r = 0.13 * (m_mensal ** 1.24)
    elif indice_regiao == 6:
        valor_r = 12.592 * (((m_mensal ** 2) / m_anual) ** 0.6030)
    elif indice_regiao == 7:
        valor_r = 68.73 * ((m_mensal ** 2 / m_anual) ** 0.841)
    elif indice_regiao == 8:
        valor_r = 19.55 + (4.20 * m_mensal)

    return valor_r


def calcular_medias(ano, mes):
    df = pd.read_excel('/Users/briancintracardoso/PycharmProjects/Erosao/Erosao_do_Solo/dados_chuva.xlsx')

    dados_filtrados = df[(df['ANO'] == ano)]

    dados_precipitacao = dados_filtrados['Precipitacao']
    lista_dados_precipitacao = []
    for i in dados_precipitacao:
        lista_dados_precipitacao.append(i)

    if mes == 'JAN':
        mes = 1
    elif mes == 'FEV':
        mes = 2
    elif mes == 'MAR':
        mes = 3
    elif mes == 'ABR':
        mes = 4
    elif mes == 'MAI':
        mes = 5
    elif mes == 'JUN':
        mes = 6
    elif mes == 'JUL':
        mes = 7
    elif mes == 'AGO':
        mes = 8
    elif mes == 'SET':
        mes = 9
    elif mes == 'OUT':
        mes = 10
    elif mes == 'NOV':
        mes = 11
    elif mes == 'DEZ':
        mes = 12

    media_mensal = lista_dados_precipitacao[mes - 1]

    media_anual = 0

    for dados in dados_precipitacao:
        media_anual += dados

    media_anual = media_anual / len(dados_precipitacao)

    return media_anual, media_mensal


x = calcular_medias(2022, 'JAN')
print(x)
