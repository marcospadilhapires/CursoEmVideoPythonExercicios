frase = input('Digite a frase: ').lower().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A ultimá letra A apareceu na posição {}'.format(frase.rfind('a')+1))
