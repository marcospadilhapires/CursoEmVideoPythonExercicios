lista = []
while True:
    lista.append(int(input("Digite um valor: ")))
    continuar = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    if continuar == "N":
        break
print("-="*70)
print(f"Foram digitados {len(lista)} valores")
lista.sort(reverse = True)
print(f"Lista em ondem decrescente: {lista}")
if 5 in lista:
    print("O valor 5 está na lista")
else:
    print("O valor 5 não está na lista")