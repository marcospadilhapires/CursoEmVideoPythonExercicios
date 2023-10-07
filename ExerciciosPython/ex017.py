import math

co = (float(input('Digite o comprimento do cateto oposto: ')))
ca = (float(input('Digite o comprimento do cateto adjacente: ')))
print('A hipotenusa é igual a {}'.format(math.hypot(co, ca)))
