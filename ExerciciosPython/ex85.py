principal = [[],[]]

for valor in range(1,8):
    dado = int(input(f"Digite o {valor}°. valor:"))

    if dado % 2 == 0:
       principal[0].append(dado)
    else:
        principal[1].append(dado)
principal[0].sort()
principal[1].sort()
print(f"Os numeros pares da lista são  {principal[0]}")
print(f"Os numeros impares da lista são {principal[1]}")

