from time import sleep
#Listas e Variaveis
alunos = list()
contador = 0
criador = 

#Funções
def pegaDados(alunos, contador):
    nome = str(input("Nome:"))
    nota1 = float(input("Nota 1:"))           
    nota2 = float(input("Nota 2:"))
    media = (nota1 + nota2)/2
    alunos.append([contador,nome,[nota1,nota2],media])

def verificaContinuar(continuar):
    while continuar not in "SN":
        continuar = str(input("Quer Continuar (S/N):").strip().upper())
    return continuar

def mostrarMediaAlunos(alunos):
    for aluno in alunos:
        print(f"{aluno[0]:<4} {aluno[1]:<15} {aluno[3]:>5.1f}")
    print("-"*60)


def mostrarNotasAluno(alunos):
    while True:
        mostrarAluno = int(input("Mostrar notas de qual aluno? (999 interrompe):"))
        if mostrarAluno == 999:
            break
        if  mostrarAluno <= len(alunos):
            print(f"Notas de {alunos[mostrarAluno][1]} são {alunos[mostrarAluno][2]}")
        else:
            print("Aluno não existe!")
        print("-"*60)    

#Programa Principal
while True:
    continuar = " "
    pegaDados(alunos, contador) 
    continuar = verificaContinuar(continuar)
    if continuar == "N":
        break
    contador += 1
print("-="*30)
print(f"{'N°':<4} {'NOME':<10} {'MÉDIA':>8}")
print("-"*60)
mostrarMediaAlunos(alunos)
mostrarNotasAluno(alunos)
print("Finalisando...")
sleep(2)
print("Volte Sempre!")




