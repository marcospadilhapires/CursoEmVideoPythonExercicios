jogador = dict()
jogador['nome'] = str(input("Nome do Jogador: "))
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
jogador['gols'] = list()
for partida in range(partidas):
    jogador['gols'].append(int(input(f"Quantos gols na partida {partida}?")))
jogador['total']= sum(jogador['gols'])
print('-='*40)
print(jogador)
print('-='*40)
for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print('-='*40)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")
for partida in range(partidas):
    print(f"   => Na partida {partida}, fez {jogador['gols'][partida]} gols")
print(f"Foi um total de {jogador['total']} gols")