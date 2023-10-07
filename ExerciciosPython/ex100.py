from random import randint
from time import sleep

def sorteia(lista):
    print("Sorteando 5 valores da lista: ",end = " ")
    while len(lista) < 5:
        num = randint(1, 10)
        lista.append(num)
        sleep(0.3)
        print(num, end=" ")
    print("Pronto")

def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f"Somando os valores pares de {lista}, temos {soma}")


#Progrma Principal

numeros = list()
sorteia(numeros)
somaPar(numeros)
