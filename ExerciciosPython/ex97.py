def escreva(texto):
    tamanho = len(texto)+4
    print("~" * tamanho)
    print(f"  {texto}  ")
    print("~" * tamanho)


#Programa Principal
escreva("Marcos")
escreva(("Curso de Python no Youtube"))
escreva("Eu sou o Mestre dos Magos")