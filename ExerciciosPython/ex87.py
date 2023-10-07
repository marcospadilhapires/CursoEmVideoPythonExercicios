matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = 0
terceiraColuna = 0
maiorValor = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]= int(input(f"Digite um valor na posição ({linha},{coluna}): "))
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
        if coluna == 2:
            terceiraColuna += matriz[linha][coluna]
        if linha == 1:
            if matriz[linha][coluna] > maiorValor:
                maiorValor = matriz[linha][coluna]

print("{:-^40}".format("Matriz"))
for linha in range(0,3):
    for coluna in range(0,3):
        print("[{:^5}]".format(matriz[linha][coluna]),end = "")
    print()
print("\n{:-^40}".format("Resultados"))
print(f"\nA)A soma de todos os valores PARES digitados foi {pares}")
print(f"B)A soma dos valores da TERCEIRA COLUNA foi {terceiraColuna}")
print(f"C)O MAIOR valor da SEGUNDA LINHA foi {maiorValor}")
