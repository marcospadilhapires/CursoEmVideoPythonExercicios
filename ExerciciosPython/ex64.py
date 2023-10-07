soma = num = contador = 0
#segundo algumas pesquisas deste modo vai ser usado mais memoria.
while num != 999:
    num = int(input("Digite um numero inteiro [999 para parar]: "))
    if num != 999:
        soma += num
        contador += 1
print("Foram digitados {} números e a soma entre eles foi {}".format(contador,soma))