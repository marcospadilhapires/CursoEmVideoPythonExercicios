pessoas = list()
somaIdades = 0
cont = 0
while True :
    print("{:-^30}".format(f"Pessoa {cont}"))
    pessoas.append({})
    pessoas[cont]["nome"] = str(input("Nome: "))
    while True:
        pessoas[cont]["sexo"]= str(input("Sexo(M,F): ").strip().upper()[0])
        if pessoas[cont]["sexo"] in "MF":
            break
        print("ERRO! Por Favor,digite apenas M ou f")
    pessoas[cont]["idade"] = int(input("Idade: "))
    somaIdades += pessoas[cont]['idade']
    print("-"*30)
    while True:
        continuar = str(input("Quer continuar?(S,N) ").strip().upper()[0])
        if continuar in "SN":
            break
        print("ERRO! Responda,digite apenas S ou N")
    if continuar == "N":
        break
    cont += 1



print("{:-^30}".format("Resultados"))
print(f"A)Foram cadastradas {len(pessoas)} pessoas")
media = somaIdades/len(pessoas)
print(f"B)A média de idade do grupo é {media:5.2f} anos")
print(f"C)São mulheres: ",end="")
for pessoa in pessoas:
    if pessoa['sexo'] == "F":
        print(pessoa['nome'],end = " ")
print(f"\nD)As pessoas com a idade igual ou acima  da média são: ")
for pessoa in pessoas:
    if len(pessoas)== 1:
        print("A lista pessoas possui apenas uma pessoa,então não existe idade acima da média")
        print(f"  nome = {pessoa['nome']}; sexo = {pessoa['sexo']}; idade = {pessoa['idade']}")
    if pessoa["idade"] >= media:
        print(f"  nome = {pessoa['nome']}; sexo = {pessoa['sexo']}; idade = {pessoa['idade']}")
