from ex108 import moeda

preço = (float(input('Digite o preço: R$')))
mais = (int(input('Digite qual a porcentagem você quer aumentar: ')))
menos = (int(input('Digite qual porcentagem você quer diminuir: ')))
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f"Aumentando {mais}%, temos {moeda.moeda(moeda.aumentar(preço, mais))}")
print(f"Reduzindo {menos}%, temos {moeda.moeda(moeda.diminuir(preço, menos))}")