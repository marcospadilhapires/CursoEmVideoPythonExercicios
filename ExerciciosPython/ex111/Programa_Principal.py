from ex111.utilidadescev import moeda
from ex111.utilidadescev import dado

preço = dado.leiaDinheiro('Digite o preço: R$')
mais = (int(input('Digite qual a porcentagem você quer aumentar: ')))
menos = (int(input('Digite qual porcentagem você quer diminuir: ')))
moeda.resumo(preço,mais,menos)