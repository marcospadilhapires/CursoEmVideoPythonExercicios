from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado

preço = dado.leiaValido('Digite o preço: R$')
mais = dado.leiaValido('Digite qual a porcentagem você quer aumentar: ')
menos = dado.leiaValido('Digite qual porcentagem você quer diminuir: ')
moeda.resumo(preço,mais,menos)