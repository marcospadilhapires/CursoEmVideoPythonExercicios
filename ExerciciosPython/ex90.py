dicionario = {}

dicionario['Nome'] = str(input('Nome: '))
dicionario['Média'] = float(input('Media: '))

if dicionario['Média'] >= 7.0:
    dicionario['Sintuação'] = 'Aprovado'
elif 5.0 <= dicionario['Média'] <7.0 :
    dicionario['Sintuação'] = 'Recuperação'
else:
    dicionario['Sintuação'] = 'Reprovado'
for k,v in dicionario.items():
    print(f"{k} é igual a {v}")