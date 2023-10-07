lista = []
for valor in range(0,5):
    lista.append(int(input(f"Digite um valor para Posição {valor}:")))
print(f"Você digitou os valores {lista}")
print(f"O maior valor digitado foi {max(lista)} nas posições",end = " ")
for cont,valor in enumerate(lista):
    if valor == max(lista):
        print(f"{cont}...",end = " ")
print(f"\nO menor valor digitado foi {min(lista)} nas posições",end = " ")
for cont,valor in enumerate(lista):
    if valor == min(lista):
        print(f"{cont}...",end = " ")