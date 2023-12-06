def boyoccos(argila, silte, areia):
    erodibilidade = ((silte + areia) / argila) / 100
    return erodibilidade


def max_perda_solo(r, k, ls, c, p1, p2):
    perda_max = r * k * ls * c * p1 * p2
    return perda_max
