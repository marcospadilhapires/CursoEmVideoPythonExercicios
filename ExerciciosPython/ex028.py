from random import randint
from time import sleep
num = randint(0,5)
print('\033[1;34m--=\033[m'*25)
print("\033[0;33mVou pensar em um numero entre 0 e 5. Tente adivinhar...\033[m")
print('\033[1;34m--=\033[m'*25)
num2 = int(input('\033[0;33mEm que número eu pensei? \033[m'))
print('PROCESSANDO...')
sleep(1)
if num == num2:
    print('\033[0;32mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print('\033[0;31mGANHEI! Eu pensei no nùmero {} e não no {}!\033[m'.format(num, num2))