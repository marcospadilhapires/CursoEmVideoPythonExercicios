from random import randint

tupla = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print("Os valores sorteados foram:",end = " ")
for c in range (0,len(tupla)):
   print(tupla[c],end = " ")
   # if c == 0:
   #     maior = tupla[c]
   #     menor = tupla[c]
   # else:
   #     if tupla[c] > maior:
   #         maior = tupla[c]
   #     elif tupla[c] < menor:
   #         menor = tupla[c]
# print(f"\nO maior valor sorteado foi {maior}")
# print(f"O menor valor sorteado foi {menor}")
print(f"\nO maior valor sorteado foi {max(tupla)}")
print(f"O menor valor sorteado foi {min(tupla)}")



