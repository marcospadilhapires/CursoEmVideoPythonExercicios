def calcularArea(largura,comprimento):
    area = largura*comprimento
    print(f"A área de um terreno {largura}x{comprimento} é de {area:.1f}m²")


print(f"{'Controle de Terrenos':^40}")
print("-"*40)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
calcularArea(l,c)
