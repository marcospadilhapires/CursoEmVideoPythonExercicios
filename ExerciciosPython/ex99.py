from time import sleep


def maior(* valores):
    tam = maior = 0
    print("-=" * 30)
    print("Analisando os valores passados...")
    for valor in valores:
        print(valor, end=" ")
        if tam == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        tam += 1
        sleep(0.3)
    print(f"Foram informados {tam} valores ao todo.")
    print(f"O maior valor informado foi {maior}.")


#Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
