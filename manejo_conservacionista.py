cultivo = {
    'Milho grão': 0.40,
    'Feijão': 0.50,
    'Oleaginosas': 0.35,
    'Hortículas': 0.50,
    'Frutíferas': 0.10,
    'Pastagem': 0.02
}

preparo = {
    'Aração de outono': 1.0,
    'Aração de primavera': 0.9,
    'Preparo com mulch': 0.60,
    'Preparo em nível': 0.35,
    'Preparo em talhões': 0.25,
    'Plantio direto': 0.25
}

pratica = {
    'Morro abaixo': 1,
    'Plantio cruzado': 0.75,
    'Plantio em nível': 0.50,
    'Plantio em faixas, cruzado': 0.37,
    'Plantio em faixas, em nível': 0.25
}

def melhor_resultado(perda_solo):
    perdas_mininimas = {}


    for cult in cultivo.keys():
        perda_solo_texte = perda_solo*cultivo[cult]
        for prep in preparo.keys():
            x = perda_solo_texte
            x = x*preparo[prep]
            for prat in pratica.keys():
                y = x
                y = y*pratica[prat]
                if y < perda_solo:
                    perdas_mininimas[cult] = f'{prep} + {prat}'


    print(perdas_mininimas)
    return perdas_mininimas

