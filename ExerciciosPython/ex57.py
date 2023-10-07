sexo = ""
while sexo != "M" and sexo != "F":
#while sexo not in 'MF':
    sexo  = input("Digite seu sexo [M/F]: ").strip().upper()[0]
    if(sexo != "M" and sexo != "F"):
        print("Dado inválido! ",end = "")
print("O sexo {} foi registrado com sucesso".format(sexo))