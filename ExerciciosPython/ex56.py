totIdades = 0
maisVelho = 0
nomeMaisVelho = ""
mulheresVinte = 0
for i in range (1, 5):
    print("----- {}ª PESSOA -----".format(i))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ").upper().strip())
    totIdades += idade

    if idade > maisVelho and sexo == "M":
        maisVelho = idade
        nomeMaisVelho = nome

    elif idade < 20 and sexo == "F":
        mulheresVinte += 1

media = totIdades / 4

print("A média de idade do grupo é de {} anos".format(media))
print("O homem mais velho tem  {} anos e se chama {}".format(maisVelho,nomeMaisVelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(mulheresVinte))