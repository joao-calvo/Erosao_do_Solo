tolerancia_perda = {
    'Latossolo': 12,
    'Argissolo': 7,
    'Nitossolo': 12,
    'Neossolo': 4
}


def boyoccos(argila, silte, areia):
    erodibilidade = ((silte + areia) / argila) / 100
    return erodibilidade


def max_perda_solo(r, k, ls, c, p1, p2):
    perda_max = r * k * ls * c * p1 * p2
    return perda_max


def ambientes_producao(classe, argila):
    if classe == 'Latossolo':
        if argila in range(35, 60):
            return 'Grupo 1'
        elif argila in range(15, 35):
            return 'Grupo 2'
    elif classe == 'Argissolo':
        return 'Grupo 3'
    elif classe == 'Neossolo':
        return 'Grupo 4'
    else:
        return 'Grupo 5'
