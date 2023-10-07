print("="*30)
print("10 TERMOS DE UMA PA")
print("="*30)


primeiro = int(input("Primeiro termo:"))
razao = int(input("Razão:"))
decimo_termo = primeiro + (10-1)* razao #formula do ultimo termo da progressão aritimética

for i in range(primeiro,decimo_termo+razao,razao):
    print(i,end = "->")

print ("Acabou")

