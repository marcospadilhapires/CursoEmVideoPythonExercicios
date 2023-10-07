jogadores = list()
jogador = dict()
gols = list()
while True:
    print("-"*40)
    jogador['nome']= str(input("Nome do Jogador: "))
    jogador['partidas']= int(input("Partidas Jogadas: "))
    for jogo in range(jogador['partidas']):
        gols.append(int(input(f"Quantos gols jogador fez na partida {jogo}:")))
    jogador['gols'] = gols[:]
    gols.clear()
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    while True:
        continuar = str(input("Quer continuar?(S/N) ").strip().upper()[0])
        if continuar in "SN":
            break
        print("Erro! Digite S ou N:")
    if continuar == 'N':
        break
print("-="*50)

# print(f"{'cod'} {'nome':<12}{'gols':<15}{'total'}")
# print("-"*40)
# for posicao,jogador in enumerate(jogadores):
#     print(f"{posicao:>3} {jogador['nome']:<12}{str(jogador['gols']):<18}{jogador['total']}")
# print("-"*40)

print("cod ",end = "")
for k in jogador.keys():
    print(f"{k:<15}",end = " ")
print()
print("-"*60)
for k,v in enumerate(jogadores):
    print(f"{k:>3}", end=" ")
    for dado in v.values():
        print(f'{str(dado):<15}', end= " ")
    print()
print("-"*60)

while True:
    mostrar = int(input("Mostrar dados de qual jogador? (999 para parar)"))
    if  mostrar < 0 or mostrar > len(jogadores)-1 :
        if mostrar == 999:
            break
        print(f"ERRO! Não  existe jogador com o código {mostrar}! Tente novamente")
        print("-" * 40)
        continue
    print("-" * 40)
    print(f"-- LEVANTAMENTO DO JOGADOR {jogadores[mostrar]['nome']}")
    for jogo in range(jogadores[mostrar]["partidas"]):
        print(f"   No jogo {jogo} fez {jogadores[mostrar]['gols'][jogo]} gols.")
    print("-" * 40)
print("<<VOLTE SEMPRE>>")