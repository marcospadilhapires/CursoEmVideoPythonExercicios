numero = int(input("Digite um número: "))

divisivel = 0


for contador in range(1,numero+1):
    if(numero % contador == 0):
        print("\033[0;33m",end = "")
        divisivel += 1
    elif(numero % contador != 0):
        print("\033[0;31m", end = "")
    print(f"{contador}",end = " ")

print("\033[0m", end = "")
print(f"\nO numero {numero} foi divisível {divisivel} vezes")

if(divisivel != 2):
    resultado = "NÃO É PRIMO!"
else:
    resultado = " É PRIMO"

print(f"E por isso ele {resultado}")