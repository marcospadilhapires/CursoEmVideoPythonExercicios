Acumulador = int(0)
Contador = int(0)
for c in range (1,501,2):
    if c % 3 == 0:
        Acumulador += c
        Contador += 1
print("A soma de todos os {} valores solicitados é {}".format(Contador,Acumulador))
