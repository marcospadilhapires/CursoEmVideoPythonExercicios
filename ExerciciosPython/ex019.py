import random

um = input('Primeiro aluno: ')
dois = input('Segundo aluno: ')
tres = input('Teceiro aluno: ')
quatro = input('Quarto aluno: ')
escolhido = random.choice([um, dois, tres, quatro])
print('O aluno escolhido foi {}'.format(escolhido))
