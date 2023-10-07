def fatorial(num, show = False):
    """
    -> Calcular o fatorial de um número
    :param num: Número que se quer calcular o fatorial
    :param show (opcional): True se quer mostrar o calulo, False(padrão) se não
    :return: Retorna o fatorial do número passado como parâmetro.
    """
    f = 1
    print("-"*30)
    for valor in range(num,0, -1):
        f *= valor
        if show:
            print(f"{valor}",end = " ")
            if valor > 1:
                print('x ',end = "")
            else:
                print("=", end = " ")
    return(f)



#Programa Principal
help(fatorial)
print(fatorial(10,True))
print(fatorial(8, True))
print(fatorial(6))
