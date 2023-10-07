num = resultado = 0
print("TABUADA")
print('-' * 20)
while True:
    cont = 1
    num = int(input("Digite um numero para descobrir sua tabuada (Número negativo para PARAR):"))
    if num < 0:
        break
    print('-' * 20)
    while cont <= 10:
        print(f'{num} x {cont} = {num * cont}')
        cont += 1
    print('-'*20)
print("Programa Tabuada Encerrado. Volte Sempre!")