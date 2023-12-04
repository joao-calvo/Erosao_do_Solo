import pandas as pd

def erosividade(regiao,m_anual,m_mensal):
    valores_r = {
    '1' : ['AM','AC','RO','RR'],
    '2' : ['PA','MT','TO'],
    '3' : 'AP',
    '4' : '',
    '5' : 'Litoral',
    '6' : 'MG',
    '7' : ['SP','MS'],
    '8' : ['PR','SC','RS']
    }

    for chave in valores_r.keys():
        if regiao in valores_r[chave]:
            indice_regiao = int(chave)


    if indice_regiao == 1 :
        valor_r = 3.76*(m_mensal**2/m_anual) + 42,77
    if indice_regiao == 2 :
        valor_r = 36.849*((m_mensal**2/m_anual)**1.0852)
    if indice_regiao == 3 :
        valor_r = (0.66*m_mensal) + 8.88
    if indice_regiao == 4 :
        valor_r = 42.307*(m_mensal**2/m_anual) + 69.763
    if indice_regiao == 5 :
        valor_r = 0.13*(m_mensal**1.24)
    if indice_regiao == 6 :
        valor_r = 12.592*(((m_mensal**2)/m_anual)**0.6030)
    if indice_regiao == 7 :
        valor_r = 68.73*((m_mensal**2/m_anual)**0.841)
    if indice_regiao == 8 :
        valor_r = 19.55 + (4.20*m_mensal)

    return valor_r

df = pd.read_excel('/Users/briancintracardoso/PycharmProjects/Erosao/Erosao_do_Solo/dados_chuva.xlsx')

ano = 2022

dados_filtrados = df[(df['ANO'] == ano)]

dados_precipitacao = dados_filtrados['Precipitacao']

media = 0
for dados in dados_precipitacao:
    media += dados

media = media/len(dados_precipitacao)






print(dados_filtrados)
print(media)



