from random import randint
from time import sleep
from operator import itemgetter

 
valores = {}
ranking = {}
for jogador in range(1,5):
    valores[f'jogador{jogador}'] = randint(1,6)

print("Valores sorteados")
for k,v in valores.items():
    print(f"    {k} tirou {v} no dado")
    sleep(1)
print("-="*30)
print("Ranking dos jogadores:")
ranking = sorted(valores.items(),key = itemgetter(1), reverse=True)

cont = 1
for jogador in ranking:
    print(f"{cont}° lugar: {jogador[0]}  com {jogador[1]}")
    cont+=1




