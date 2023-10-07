def leiaInt(texto):
   while True:
        num = str(input(texto))
        if num.isnumeric():
            return num
            break
        else:
            print("\33[31m ERRO!Digite um número inteiro válido\33[m")


#Programa Principal
n = leiaInt('Digite um número:')
print(f"Você acabou de digitar o número {n}")


