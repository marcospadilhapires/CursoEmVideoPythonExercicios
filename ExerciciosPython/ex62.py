print("Gerador de PA")
print("-="*10)
primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
termo = primeiro
contador = 0
novosTermos = 1
limite = 10
while contador < limite or novosTermos != 0:
    print(" {}".format(termo),end = "")
    print(" ->",end = "")
    termo += razao
    contador += 1
    if(contador == limite):
        print(" PAUSA",end = "")
        novosTermos = int(input("\nQuantos termos você quer mostrar a mais?"))
        limite += novosTermos
print("Progressão finalizada com {} termos mostrados.".format(contador))
