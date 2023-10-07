lista = []
continuar = ""
while continuar != 'N':
    num = int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar...")
    continuar = str(input("Quer Continuar? [S/N] ").strip().upper() [0])
print("-="*70)
print(f"Você digitou os valores {sorted(lista)}")