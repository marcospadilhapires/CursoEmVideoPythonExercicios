num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases de conversão:
[ 1 ] converter para BINÁRIO 
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    resultado = bin(num)
    tipo = 'BINÁRIO'

elif opcao == 2:
    resultado = oct(num)
    tipo = 'OCTAL'

elif opcao == 3:
    resultado = hex(num)
    tipo = 'HEXADECIMAL'
else:
    print('Opção Inválida, tente novamente!')
    exit()

print('{} convertido para {} é igual a {}'.format(num, tipo, resultado[2:]))