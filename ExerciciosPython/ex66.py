valores = soma = cont = 0

while True:
    valores = int(input("Digite um valor: (999 para parar): "))
    if valores == 999:
        break
    soma += valores
    cont += 1
print(f"A soma dos {cont} foi {soma}!")