lista = []
par = []
impar = []
while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    # if valor % 2 == 0:
    #     par.append(valor)
    # else:
    #     impar.append(valor)
    continuar = str(input("Quer Continuar?[S/N] ").strip())
    if continuar in 'Nn':
        break
for valor in lista:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print('-='*50)
print(f"A lista completa é {lista}")
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')