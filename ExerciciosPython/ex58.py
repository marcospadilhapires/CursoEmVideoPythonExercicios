from random import randint
from time import sleep
num = int(randint(0,10))
contador = 1
print("Pensando...")
sleep(2)
print("Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi ?")
palpite = int(input("Tente adivinhar o número: "))
while palpite != num:
    contador += 1
    if(palpite > num):
        print("O número é menor!")
        palpite = int(input("Tente novamente: "))
    elif(palpite < num ):
        print("O número é maior!")
        palpite = int(input("Resposta errada,tente novamente: "))
print("Acertou! o numero correto é {} e foram necessários {} palpites para vencer".format(palpite,contador))