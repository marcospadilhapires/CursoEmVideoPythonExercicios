from ex109 import moeda

preço = (float(input('Digite o preço: R$')))
mais = (int(input('Digite qual a porcentagem você quer aumentar: ')))
menos = (int(input('Digite qual porcentagem você quer diminuir: ')))
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço, True)}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}')
print(f"Aumentando {mais}%, temos {moeda.aumentar(preço, mais, True)}")
print(f"Reduzindo {menos}%, temos {moeda.diminuir(preço, menos, True)}")