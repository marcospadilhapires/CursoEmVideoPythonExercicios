def voto(nasc=0):
    """
    :param nasc: ano de nascimento
    :return: "Com {idade} anos: {voto}."
    """
    from datetime import datetime
    idade = datetime.now().year - nasc
    if nasc == 0:
        return "Não foi informado o ano de nascimento"
    else:
        if idade < 16:
            voto = str("Não Vota!")
        elif 16 <= idade < 18 or idade >= 65:
            voto = str("Voto Opcional.")
        elif idade >= 18:
            voto = str("Voto obrigatorio!")
        return f"Com {idade} anos: {voto}."


# Programa Principal
print("-" * 50)
ano = int(input("Em que ano você nasceu? "))
print(voto(ano))
