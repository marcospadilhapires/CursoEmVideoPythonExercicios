tupla = (int(input('Digite um número:')),
        int(input('Digite outro número:')),
        int(input('Digite mais um  número:')),
        int(input('Digite o ultimo número:')))
cont = 0
print(f'Você digitou os valores {tupla}')
print(f'o valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'Os valor 3 apareceu na {tupla.index(3)+1}° posição')
else:
    print(f'Não apareceu o valor 3 ')

print('Os valores pares digitados foram:',end = " ")
for c in range(0,len(tupla)):
    if tupla[c] % 2 == 0:
        print(tupla[c],end = " ")
        cont += 1
if cont == 0:
    print('nem um')
