print('{:=^40}'.format(' LOJAS '))
p = float(input("Preço das Compras: R$"))
print('''FORMAS DE PAGAMENTOS
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão''')
op = int(input("Qual a sua opção? "))

if op == 1:
    f =float(p-(p*0.1))

elif op == 2:
    f = float(p - (p * 0.05))

elif op == 3:
    c = p/2
    f = p
    print('Sua compra sera parcelada em 2x de R${}'.format(c))
elif op == 4:
    qp = int(input("Quantidade de Parcelas: "))
    f =  p+(p*0.20)
    c = f / qp
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(qp,c))
else:
    print("OPÇÃO INVÁLIDA DE PAGAMENTO!")
    exit()

print("Sua Compra de R${:.2f} vai custar R${:.2f} no final".format(p,f))

