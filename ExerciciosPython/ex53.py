# função (upper) para deixar letras em maiusculos e função (strip) para remover espaço do começo e no final da frase.
frase = str(input("Digite uma frase: ")).strip().upper()

# dividido a frase por letras,tranformando em uma lista utilizando a função (split)
frasePalavras = frase.split()

# juntando a letras separadas sem espaços('') utilizando a função (join)
fraseJunto = ''.join(frasePalavras)

# armazenando na variavel inverso a frase de inversa.
inverso = fraseJunto[:: -1]

# armazenando na variavel inverso a frase de inversa.
#for letra in range(len(fraseJunto) -1,-1,-1):
   # inverso += fraseJunto[letra]

print(f"O inverso de {fraseJunto} é {inverso}")

if(fraseJunto == inverso):
    print("Temos um palíndromo!")

else:
    print("A frase digitada não é um palíndromo!")


