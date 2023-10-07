l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo Lado: '))
l3 = float(input('Terceiro Lado: '))

if l1+l2>l3 and l2+l3>l1 and l1+l3>l2:
    print('Os lados PODEM FORMAR um triângulo', end = " ")

    if l1 == l2 == l3:
        print('EQUILATERO ')

    elif l1 == l2 != l3 or l2 == l3 != l1 or l3 == l1 != l2:
        print("ISÓCELES")

    elif l1 != l2 != l3 != l1:
        print("ESCALENO")
else:
    print('Os lados NÃO PODEM FORMAR um TRIÂNGULO')