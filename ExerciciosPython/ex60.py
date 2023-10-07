from math import factorial

num = int(input("Digite um numero: "))
resultado = 1
print( "{}! = {}".format(num,num),end = " ")
#resultado = factorial(num)
while(num > 1):
#for num in range(num,1,-1):
    resultado *= num
    num -= 1
    print("x {}".format(num),end = " ")

print("= {}".format(resultado))