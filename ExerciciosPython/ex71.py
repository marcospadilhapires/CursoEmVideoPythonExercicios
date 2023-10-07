valor = int(input("Qual o valor você quer sacar? R$"))
cedula = 0
contador = 0

#Primeira Forma
# notas50 = int(valor/50)
# valorResto = int(valor % 50)
# if notas50 > 0:
#         print(f"Total de {notas50} cédulas de R$50")
# notas20 = int(valorResto/20)
# valorResto = int(valorResto % 20)
# if notas20 > 0:
#     print(f"Total de {notas20} cédulas de R$20")
#
# notas10 = int(valorResto / 10)
# valorResto = int(valorResto % 10)
# if notas10 > 0:
#     print(f"Total de {notas10} cédulas de R$10")
#
# notas1 = int(valorResto/ 1)
# valorResto = int(valorResto % 1)
# if notas1 > 0:
#     print(f"Total de {notas1} cédulas de R$1")


while True:
    if contador == 0:
        cedula = 50
        notas = int(valor/ cedula)
        valorResto = int(valor % cedula)
    else:
        if contador == 1:
            cedula = 20
        elif contador == 2:
            cedula = 10
        elif contador == 3:
            cedula = 1
        elif contador >= 4:
            break
        notas = int(valorResto / cedula)
        valorResto = valorResto % cedula
    if notas != 0:
        print(f"Total de {notas} notas de R${cedula}")
    contador += 1
print("Volte sempre ao Banco do Marcão!Tenha um bom dia!")

