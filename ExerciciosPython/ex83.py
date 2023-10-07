
pilha = []
expressao = str(input("Digite uma expressão: "))


for c in expressao:
    if c == "(":
         pilha.append("(")
    elif c == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressão está correta")
else:
    print("Sua expressão não está correta")



