from random import randint
from time import sleep

escolha = int(input('''Digite sua escolha 
[1] PEDRA
[2] PAPEL
[3] TESOURA
ESCOLHA:'''))

escolha2 = randint(1,3)
print("-="*12)
print("PEDRA")
sleep(0.5)
print("PAPEL")
sleep(0.5)
print("TESOURA")
sleep(0.5)
print("-="*12)
if escolha == 1:
    if escolha2 == 2:
        print('''Você perdeu! Máquina escolheu Papel e você Pedra!''')
    elif escolha2 == 3:
        print('''Você Ganhou! Máquina escolheu Tesoura e você Pedra!''')
    elif escolha2 == 1:
        print('''Empatou! Máquina escolheu Pedra e você Pedra!''')

elif escolha == 2:
    if escolha2 == 2:
        print('''Empatou! Máquina escolheu Papel e você Papel!''')
    elif escolha2 == 3:
        print('''Você Perdeu! Máquina escolheu Tesoura e você Papel!''')
    elif escolha2 == 1:
        print('''Você Ganhou! Máquina escolheu Pedra e você Papel!''')

elif escolha == 3:
    if escolha2 == 2:
        print('''Você Ganhou! Máquina escolheu Papel e você Tesoura!''')
    elif escolha2 == 3:
        print('''Empatou! Máquina escolheu Tesoura e você Tesoura!''')
    elif escolha2 == 1:
        print('''Você Perdeu! Máquina escolheu Pedra e você Tesoura!''')

else:
    print('Escolha inválida')
