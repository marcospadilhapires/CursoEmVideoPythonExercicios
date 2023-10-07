num = int(input('Diga um número: '))
if num % 2 == 0:
    escolha = 'PAR'
else:
    escolha = 'ÍMPAR'
print('O número {} é {}'.format(num, escolha))
