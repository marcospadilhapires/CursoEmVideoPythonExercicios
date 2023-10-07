def metade(valor=0,formatado = False):
    """
    -> Calcula a metade do valor.
    :param valor: valor que usuário passou
    :param formatado: True para formatar  o valor como dinheiro.
    :return: Metade do valor.
    """
    v = valor / 2
    if formatado:
        v = moeda(v)
    return v


def dobro(valor=0, formatado = False):
    """
    -> Calcula o dobro do valor.
    :param valor: Valor
    :param formatado: True para formatar  o valor como dinheiro.
    :return: Dobro do valor
    """
    v = valor * 2
    if formatado:
        v = moeda(v)
    return v


def aumentar(valor=0, porcentagem=0, formatado = False):
    """
    -> Aumenta o valor na porcentagem que usuário definir
    :param valor: Valor
    :param porcentagem: Quantos porcento se quer aumentar
    :param formatado: True para formatar  o valor como dinheiro.
    :return: O valor com o aumento.
    """
    v = valor + (valor / 100 * porcentagem)
    if formatado:
        v = moeda(v)
    return v


def diminuir(valor=0, porcentagem=0, formatado = False):
    """
    -> Diminui o valor na porcentagem que usuário definir
    :param valor: Valor
    :param porcentagem: Quantos porcento se quer diminuir
    :param formatado: True para formatar  o valor como dinheiro.
    :return: O valor com a redução.
    """
    v = valor - (valor / 100 * porcentagem)
    if formatado:
        v = moeda(v)
    return v


def moeda(valor=0, unidade="R$"):
    """
    -> Formata o valor como moeda com unidade a frente e separado por vírgula
    :param valor: Valor
    :param unidade: Unidade pmostrada antes do valor
    :return: valor formatado.
    """
    moeda = (f"{unidade}{valor:.2f}")
    moeda = moeda.replace('.', ',')
    return moeda
