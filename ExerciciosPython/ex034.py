salario = float(input('Digite o salário do funcionário: '))
if salario>1250:
    novo = (salario*10/100)+salario
else:
    novo = (salario*15/100)+salario

print('Quem ganhava R${} agora vai ganhar R${}'.format(salario, novo))