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


def calcular_medias_anual(ano):
    df = pd.read_excel('/Users/briancintracardoso/PycharmProjects/Erosao/Erosao_do_Solo/dados_chuva.xlsx')

    dados_filtrados = df[(df['ANO'] == ano)]

    dados_chuva = {}
    media_anual = 0

    for dados in dados_filtrados.values:
        year, mes_1, media = dados
        dados_chuva[mes_1] = media

    for dados in dados_chuva.keys():
        media_anual += int(dados_chuva[dados])

    media_anual = media_anual / len(dados_chuva)

    return media_anual


def calcular_media_mensal(ano, mes):
    df = pd.read_excel('/Users/briancintracardoso/PycharmProjects/Erosao/Erosao_do_Solo/dados_chuva.xlsx')

    dados_filtrados = df[(df['ANO'] == ano)]

    dados_chuva = {}

    for dados in dados_filtrados.values:
        year, mes_1, media = dados
        dados_chuva[mes_1] = media

    return dados_chuva[mes]


'''

y = ['JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']
x =[]
z=[]
for mes in y:
    x.append(calcular_medias(2022,mes))

for dado in x:
    z.append(erosividade('SP',dado[0],dado[1]))
soma = 0
for a in z:
    soma += a
print(x)
print(z)
print(soma)
print(soma/100)

'''
