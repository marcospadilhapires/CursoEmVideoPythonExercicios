def leiaValido(texto):
    while True:
        valor = str(input(texto).strip().replace(",","."))
        if valor.replace(".","").isnumeric():
            break
        else:
            print(f"\33[31mERRO! '{valor}' é um valor um inválido\33[m")
    return float(valor)