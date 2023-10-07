num = int(input("Digite um numero qualquer: "))
primeiro = 0
segundo = 1
contador = 1
while contador <= num:
    terceiro = primeiro + segundo
    print(" {} ->".format(primeiro),end = "")
    primeiro = segundo
    segundo = terceiro
    contador += 1
print(" FIM",end = "")


