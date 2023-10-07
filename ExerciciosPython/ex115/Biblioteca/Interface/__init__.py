from time import sleep

def leiaOpcao(msg):
    while True:
        try:
            opção = int(input(msg))
        except (ValueError, TypeError):
            print("\33[0:31mERRO: por favor, digite um número inteiro válido\33[m")
            continue
        else:
            return opção
def titulo(msg):
    traços = 50
    print("-"* traços)
    print(f"{msg:^{traços}}")
    print("-" * traços)

def imprimirlinha(n = 50):
    print("-"*n)

def Menu(lista):
    titulo("MENU PRINCIPAL")
    c = 1
    for opcao in lista:
        print(f"\33[33m{c}\33[m - \33[34m{opcao}\33[m")
        c += 1
    imprimirlinha()
    return leiaOpcao("\33[33mSua Opção:\33[m")



