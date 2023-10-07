total = 0
cont = 0
for contador in range(1,7):
    numero = int(input("Digite um numero inteiro: "))
    if (numero % 2 == 0):
        total += numero
        cont += 1

print(f"Você informou {cont} numeros pares e a soma foi {total}")


