from time import sleep
import os

print("=-=-=-=-EXERCÍCIO 59-=-=-=-=")
v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))
escolha = 0
while escolha != 5:
    print("""=-=-=-=-=-MENU-=-=-=-=-=
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa""")
    escolha = int(input("Digite sua escolha: "))

    if escolha == 1:
        soma = v1 + v2
        print("------ Resultado ------")
        print("A Resultado de {} + {} foi {}".format(v1,v2,soma))

    elif escolha == 2:
        print("------ Resultado ------")
        multiplicacao = v1 * v2
        print("O resultado de {} x {} foi {}".format(v1, v2, multiplicacao))

    elif escolha == 3:
        maior = 0
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print("------ Resultado ------")
        print("O numero maior entre {} e {} é {}".format(v1,v2,maior))

    elif escolha == 4:
        print("------ Resultado ------")
        print("Digite outros valores:")
        v1 = float(input("Digite o primeiro valor: "))
        v2 = float(input("Digite o segundo valor: "))
        print("agora os valores são {} e {}".format(v1,v2))

    elif escolha == 5:
        print("Saindo do Programa...")
        sleep(2)

    else:
        print("Essa escolha não existe! Digite uma das 5 opções apresentadas:")
        print("=-=" * 10)

print("Fim do programa,volte sempre!")

