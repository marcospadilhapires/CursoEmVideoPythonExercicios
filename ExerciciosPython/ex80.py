lista = []
posicao = 0
for valor in range(0,5):
   num = int(input("Digite um valor: "))
   if valor == 0 or num > max(lista):
       lista.append(num)
       print("Adicionado ao final da lista...")
   else:
       for valor in lista:
           if num > valor:
               posicao = lista.index(valor) + 1
           else:
               lista.insert(posicao, num)
               print(f"Adicionando na posição {posicao} da lista")
               posicao = 0
               break

print(f"Os valores da lista são {lista}")