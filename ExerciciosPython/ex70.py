total = maismil = contador = 0
print("-"* 40)
print("{:^40}".format("LOJA DO POVO"))
print("-"* 40)
while True:
    nome = str(input("Digite o nome do Produto: "))
    preco = float(input("Digite o preço do produto: R$"))
    continuar = ' '
    total += preco
    if preco > 1000:
        maismil += 1
    if contador == 0 or preco < baratopreco:
        baratonome = nome
        baratopreco = preco
    contador += 1
    while continuar not in 'SN':
        continuar = str(input("Quer continuar?[S/N]").strip().upper() [0])
    if continuar == "N":
        break
print('{:-^40}'.format("Estatísticas"))
print(f"O total gasto na compra foi {total:.2f}")
print(f" tivemos {maismil} produtos custando mais de R$1000")
print(f"O produto mais barato foi o {baratonome} custando R${baratopreco:.2f}")