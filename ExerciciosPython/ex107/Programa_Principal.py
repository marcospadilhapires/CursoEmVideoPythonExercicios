from ex107 import moeda

preço = (float(input('Digite o preço: R$')))
mais = (int(input('Digite qual a porcentagem você quer aumentar: ')))
menos = (int(input('Digite qual porcentagem você quer diminuir: ')))
print(f'A metade de {preço} é {moeda.metade(preço)}')
print(f'O dobro de {preço} é {moeda.dobro(preço)}')
print(f"Aumentando {mais}%, temos {moeda.aumentar(preço, mais)}")
print(f"Reduzindo {menos}%, temos {moeda.diminuir(preço, menos)}")