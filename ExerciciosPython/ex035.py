l1 = float(input('Primeiro valor: '))
l2 = float(input('Segundo valor: '))
l3 = float(input('Terceiro valor: '))
if (l1 + l2) > l3 and (l2 + l3) > l1 and (l3 + l1) > l2:
    r = 'PODEM FORMAR'
else:
    r = 'NÃO PODEM FORMAR'
print('Os seguementos acima {} um triângulo'.format(r))