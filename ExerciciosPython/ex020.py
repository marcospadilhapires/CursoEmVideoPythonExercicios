import random

um = input('Priemeiro Aluno: ')
dois = input('Segundo Aluno: ')
tres = input('Terceiro Aluno: ')
quatro = input('Quarto Aluno: ')
escolhido = [um, dois, tres, quatro]
random.shuffle(escolhido)
print('A ordem de apresentação será')
print(escolhido)
