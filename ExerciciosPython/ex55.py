maior = 0
menor = 0
meio  = 0

for i in range(1,6):
    peso = float(input("Peso da {}ª pessoa: ".format(i)))
    #resolução minha:
    # if (peso > maior):
    #     meio = maior
    #     maior = peso
    #     if(menor == 0):
    #         menor = meio
    #     elif(meio < menor):
    #         menor = meio
    # else:
    #     meio = peso
    #     if (menor == 0):
    #         menor = meio
    #     elif (meio < menor):
    #         menor = meio

    #resolução guanabara

    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso lido foi de {}Kg".format(maior))
print("O maior peso lido foi de {}Kg".format(menor))