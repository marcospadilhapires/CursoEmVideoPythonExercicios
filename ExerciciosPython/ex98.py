from  time import sleep

def contador(inicio,fim,passo):
    print("-="*40)
    if abs(passo) == 0:
        passo = 1
    print(f"Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}")
    if inicio < fim:
        fim +=1
    elif inicio>fim:
        fim -=1
        if passo < 0:
            passo = passo
        else:
            passo = -passo
    for num in range(inicio, fim, passo):
        print(num, end=" ", flush = True)
        sleep(0.5)
    print("FIM!")


#Programa Principal
contador(1,10,1)
contador(10,0,2)
print("-="*40)
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)