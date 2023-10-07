def metade(valor=0,formatado = False):
    """
    -> Calcula a metade do valor.
    :param valor: valor que usuário passou
    :param formatado: True para formatar  o valor como dinheiro.
    :return: Metade do valor.
    """
    v = valor / 2
    return moeda(v) if formatado else v


def dobro(valor=0, formatado = False):
    """
    -> Calcula o dobro do valor.
    :param valor: Valor
    :param formatado: True para formatar  o valor como dinheiro.
    :return: Dobro do valor
    """
    v = valor * 2
    return moeda(v) if formatado else v


def aumentar(valor=0, porcentagem=0, formatado = False):
    """
    -> Aumenta o valor na porcentagem que usuário definir
    :param valor: Valor
    :param porcentagem: Quantos porcento se quer aumentar
    :param formatado: True para formatar  o valor como dinheiro.
    :return: O valor com o aumento.
    """
    v = valor + (valor / 100 * porcentagem)
    return moeda(v) if formatado else v


def diminuir(valor=0, porcentagem=0, formatado = False):
    """
    -> Diminui o valor na porcentagem que usuário definir
    :param valor: Valor
    :param porcentagem: Quantos porcento se quer diminuir
    :param formatado: True para formatar  o valor como dinheiro.
    :return: O valor com a redução.
    """
    v = valor - (valor / 100 * porcentagem)
    return moeda(v) if formatado else v


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

def resumo(valor = 0,aumento = 0,redução = 0):
    """
    -> Mostra na tela um resumo com a  metade e o dobro do valor, valor com o aumento e valor com a redução
    :param valor: valor
    :param aumento: Quantos porcento se quer aumentar
    :param redução: Quantos porcento se quer diminuir
    :return: Resumo formatado.
    """
    resumo = {"Preço analisado": moeda(valor),
              "Dobro do preço": dobro(valor,True),
              "Metade do preço":metade(valor,True),
              f"{aumento}% de aumento": aumentar(valor,aumento,True),
              f"{redução}% de redução": diminuir(valor,redução,True)}
    print("-" * 40)
    print(f"{'RESUMO DO VALOR':^40}")
    print("-" * 40)
    for k,v in resumo.items():
        print(f"{k+':':<30}{v}")
    print("-" * 40)
