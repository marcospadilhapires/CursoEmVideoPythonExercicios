n1 = float(input("Primeira Nota: "))
n2 = float(input('Segunda Nota: '))
m = (n1 + n2) /2
print('Tirando {:.1f} e {:.1f} tem a média {:.1f}'.format(n1, n2, m))
if m >= 7:
    print("O aluno está APROVADO!")
elif 7 > m >= 5:
    print('O aluno ficou de RECUPERAÇÃO!')
else:
    print('O aluno foi REPROVADO!')
