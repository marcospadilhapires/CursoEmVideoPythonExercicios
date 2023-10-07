tupla = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,
         'Tranferidor',4.40,'Compasso',9.99,'Mochila',120.32,
         'Canetas',22.30,'Livro',34.90)

print('-'*40)
print("{:^40}".format("LISTAGEM DE PREÇOS"))
print('-'*40)
for c in range(0, len(tupla)):
    if c % 2 == 0:
        print("{:.<30}".format(tupla[c]),end = " ")
    else:
        print("R${:7.2f}".format(tupla[c]))
print('-'*40)