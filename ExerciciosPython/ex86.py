matriz = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        num = int(input(f"Digite um valor para posição [{i},{j}]:"))
        matriz[i][j] = num
for i in range(0,3):
    print(end = "\n")
    for j in range(0,3):
            print("[{:^5}]".format(matriz[i][j]),end ="")


