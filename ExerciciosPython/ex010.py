n = float(input('Digite quanto dinheiro você tem na carteira? '))
d = float(input('Digite quanto vale o dolar atual:'))
print('Com R${} você pode comprar U${:.2f}'.format(n, n/d))