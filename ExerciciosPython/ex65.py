escolha = "S"
soma = num = contador = maior = menor = 0
while escolha in "sS":
    num = int(input("Digite um numero inteiro: "))
    soma += num
    if contador == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    contador += 1
    escolha = str(input("Quer continuar a digitar valores? [S/N] ").strip() [0])
media = float(soma/contador)
print("-="*10)
print('''Você digitou {} números
A média dos valores digitados foi {:.2f}
O maior valor foi {}
O menor valor foi {}'''.format(contador,media,maior,menor))
