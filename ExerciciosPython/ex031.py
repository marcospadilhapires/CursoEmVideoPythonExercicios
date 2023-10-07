d = float(input('Qual a distancia da sua viagem em km: '))
p = d*0.45 if d>200 else d*0.50
print('Você está prestes a começar uma viagem de {:.2f}Km'.format(d))
print("E o preço da sua passagem será de R${:.2f}".format(p))