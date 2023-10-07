from random import randint
from time import sleep
jogos = []
print("-"*40)
print("{:^40}".format("JOGA NA MEGA SENA"))
print("-"*40)
qjogos = int(input("Quantos jogos você quer que eu sorteie? "))
for jogo in range(qjogos):
    jogos.append([])
    for numero in range(0,7):
        while True:
            num = randint(0,60)
            if num not in jogos[jogo]:
                jogos[jogo].append(num)
                break
print(f"-=-=-= SORTEANDO {qjogos} JOGOS -=-=-=".format())
for jogo in range(qjogos):
    jogos[jogo].sort()
    print(f"Jogo {jogo+1}:{jogos[jogo]}")
    sleep(1)
print("-=-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=-=")

