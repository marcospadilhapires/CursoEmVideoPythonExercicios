from random import randint
#introdução
print("=-"*15)
print("VAMOS JOGAR PAR OU IMPAR")
print("=-"*15)
vitorias = 0
while True:
    num = int(input("Diga um valor: "))
    computador = randint(0,11)
    total = num + computador
    escolha = ' '
    while(escolha not in 'PI'):
        escolha = str(input("Par ou Impar [P/I]: ").upper().strip() [0])
    print("-" * 30)
    print(f"Você jogou {num} eo computador {computador}. Total de {total} ",end = "")
    print("DEU PAR" if total % 2 == 0 else "DEU IMPAR")
    print("-" * 30)
    if escolha == "P":
        if total % 2 == 0:
            print("Você VENCEU!")
            print("Vamos jogar novamente...")
            print("=-" * 15)
            vitorias += 1
        else:
            print("Você PERDEU!")
            print("=-" * 15)
            break
    elif escolha == "I":
        if total % 2 != 0:
            print("Você VENCEU!")
            print("Vamos jogar novamente...")
            print("=-" * 15)
            vitorias += 1
        else:
            print("Você PERDEU!")
            print("=-" * 15)
            break
print(f"GAME OVER! Você venceu {vitorias} vezes")

