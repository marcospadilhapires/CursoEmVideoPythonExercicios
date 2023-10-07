print("Gerador de PA")
print("-="*10)
primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
PA = primeiro
contador = 1
while contador <= 10:
    print("{}".format(PA),end = "")
    print("-> " if contador <= 9 else " -> Acabou",end ="")
    PA += razao
    contador += 1