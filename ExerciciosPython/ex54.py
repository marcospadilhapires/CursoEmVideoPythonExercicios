from datetime import date # importando modulo para ano atual.

maiores = 0
menores = 0
atual = date.today().year #ano do dia atual.
for i in range(1,8):
    nasc = int(input("Em que ano a {}ª pessoa nasceu? ".format(i)))
    idade = atual - nasc
    if(idade >=18):
        maiores += 1
    else:
        menores += 1

print("Ao todo tivemos {} pessoas maiores de idade".format(maiores))
print("E tambem tivemos {} pessoas menores de idade".format(menores))