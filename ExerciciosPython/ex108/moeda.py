def metade(valor=0):
    v = valor / 2
    return v


def dobro(valor=0):
    v = valor * 2
    return v


def aumentar(valor=0, porcentagem=0):
    v = valor + (valor / 100 * porcentagem)
    return v


def diminuir(valor=0, porcentagem=0):
    v = valor - (valor / 100 * porcentagem)
    return v


def moeda(valor=0, unidade="R$"):
    moeda = (f"{unidade}{valor:.2f}")
    moeda = moeda.replace('.', ',')
    return moeda
