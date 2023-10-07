from time import sleep


def titulos(titulo, corfundo, corletra=47):
    traços = int(len(titulo) + 4)
    print(f"\33[{corletra}:{corfundo}m~" * traços)
    print(f"  {titulo}  ")
    print("~" * traços)
    print("\33[m", end="")


def escolha_funcao(texto):
    funcao = input(texto)
    sleep(0.5)
    if funcao.strip().upper() == "FIM":
        titulos("ATÉ LOGO", 41)
        return True
    else:
        titulos(f"Acessando o manual do comando '{funcao}'", 42)
        sleep(1)
        print("\33[7:40m")
        help(funcao.strip().lower())
        print("\33[m", end="")


def menu():
    sleep(0.5)
    titulos("SISTEMA DE AJUDA PyHELP", 44)


# Programa Principal
while True:
    menu()
    if escolha_funcao("Função ou Biblioteca >"):
        sleep(0.3)
        break
