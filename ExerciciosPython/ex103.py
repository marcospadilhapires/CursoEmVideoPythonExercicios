def ficha(n ="<desconhecido>",g = 0):
    return f"O jogador {n} fez {g} gol(s) no campeonato."


#Programa Principal
Nome = (input("Nome do Jogador: "))
Gols = (input("Número de Gols: "))

if Nome.strip() == '' and Gols.strip() == '':
    print(ficha())
elif Nome.strip() == '' and Gols.isnumeric():
    print(ficha(g = Gols))
elif Nome != '' and Gols == '':
    print(ficha(n = Nome))
elif Nome != '' and not Gols.isnumeric():
    print(ficha(n= Nome))
else:
    print(ficha(Nome,Gols))

