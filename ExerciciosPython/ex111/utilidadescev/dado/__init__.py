def leiaDinheiro(texto):
    while True:
        valor = str(input(texto).strip())
        if valor.replace(",","").isnumeric() or valor.replace(".","").isnumeric():
            break
        else:
            print("\33[31mERRO! Digite um valor válido\33[m")
    return float(valor)