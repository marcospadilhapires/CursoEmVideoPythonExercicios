from datetime import date
Nasc = int(input('Ano de Nascimento: '))
Atual = int(date.today().year)
idade = Atual - Nasc
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print("Classificação:MIRIM")
elif idade <= 14:
    print("Classificação:INFANTIL")
elif idade <= 19:
    print('Classificação:JÚNIOR')
elif idade <= 25:
    print("Classificação:SÊNIOR")
elif idade > 25:
    print("Classificação:MASTER")