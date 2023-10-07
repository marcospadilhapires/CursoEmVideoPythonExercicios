print("ANÁLISE DE DADOS")
maiores = homens = mulheres20 = 0
contador = 1
while True:
    print('-'*7 + f'Pessoa {contador}'+'-'*7)
    idade = int(input("Digite a idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa [M/F]').upper().strip()[0])
    if idade >= 18:
        maiores += 1

    if sexo == "M":
        homens += 1

    if sexo == "F" and idade <= 20:
        mulheres20 += 1

    print("Pessoa cadastrada com sucesso!")
    contador += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input("Quer continuar? [S/N]:").upper().strip()[0])
    if continuar == "N":
        break
print('-'*7 + f' Resultados '+'-'*7)
print(f'''Das pessoas cadastradas:
{maiores} possuem mais de 18 anos.
{homens} são homens.
{mulheres20} são mulheres com menos de 20 anos.''')
