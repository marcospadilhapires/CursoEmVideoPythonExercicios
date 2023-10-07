from datetime import date
sexo = str(input("Digite seu sexo(M -> Masculino e F -> Feminino):"))
if sexo == "F" or sexo == "f":
    print("Você não precisa fazer alistamento melitar!")
    exit()
elif sexo == "M" or sexo == "m":
    ano = int(date.today().year)
    anoN = int(input('Ano de Nascimento:'))
    idade = int(ano - anoN)
    print("Quem nasceu em {} tem {} anos em {}".format(anoN, idade, ano))
    if idade < 18:
        print("Ainda faltam {} anos para o alistamento".format(18-idade))
        print('Seu alistamento sera em {}'.format(ano + (18-idade)))
    elif idade == 18:
        print("Aliste-se IMEDIATAMENTE!!")
    else:
        print("Voce ja deveria ter se alistado a {} anos".format(idade - 18))
        print('Seu alistamento foi em {}'.format(ano - (idade - 18)))
else:
    print("Erro,esse sexo não existe!")