ListaPrincipal = []
dados = []
maiorIdade = 0
nomesMaior = []
menorIdade = 0
nomesMenor = []
while True:
    dados.append(input("Nome: "))
    dados.append(input("idade: "))
    ListaPrincipal.append(dados[:])
    continuar = str(input("Você deseja continuar [S/N]: ").strip().upper())
    if continuar == "N":
        break
    dados.clear()
print("-="*60)
print(f"Ao todo, você cadastrou {len(ListaPrincipal)} pessoas")
for c in ListaPrincipal:
    if ListaPrincipal[0] == c:
        maiorIdade = c[1]
        menorIdade = c[1]
        nomesMaior.append(c[0])
        nomesMenor.append(c[0])
    elif c[1] > maiorIdade:
        maiorIdade = c[1]
        nomesMaior.clear()
        nomesMaior.append(c[0])
    elif c[1] == maiorIdade:
        nomesMaior.append(c[0])
    elif c[1] < menorIdade:
        menorIdade = c[1]
        nomesMenor.clear()
        nomesMenor.append(c[0])
    elif c[1] == menorIdade:
        nomesMenor.append(c[0])
print(f"O maior idade foi de {maiorIdade}. idade de ",end = "")

for nome in nomesMaior:
    print(nome,end = " ")

print(f"\nA menor idade foi de {menorIdade}. idade de ",end = "")

for nome in nomesMenor:
    print(nome,end = " ")