valorcasa = float(input('Valor da casa:'))
salario = float(input('Salário do comprador:'))
anos = int(input('Quantos anos de financiamento:'))
prestacao = valorcasa/(anos*12)
partesalario = 30/100 * salario

if prestacao>partesalario:
    print('Emprétimo negado, a prestação mensal de R${:.2f} excede 30% do salário atual.'.format(prestacao))

else:
    print('Emprestimo aceito,você pagará R${:.2f} por mês em {} anos '.format(prestacao,anos))