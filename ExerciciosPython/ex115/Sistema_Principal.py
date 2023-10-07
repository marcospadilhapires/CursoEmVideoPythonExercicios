from ex115.Biblioteca.Interface import *
from ex115.Biblioteca.Arquivos import *
from time import sleep

while True:
    try:
        op = Menu(["Ver Pessoas Listadas","Cadastrar nova Pessoa","Remover Registro","Sair do sistema"])
        if op == 1:
            titulo("PESSOAS CADASTRADAS")
            lerArquivo("dados.txt")
        elif op == 2:
            titulo("NOVO CADASTRO")
            nome = str(input("Nome: "))
            idade = int(leiaOpcao("Idade: "))
            adicionardados("dados.txt",nome, idade)
        elif op == 3:
            titulo("REMOVER REGISTRO")
            if lerArquivo("dados.txt"):
                imprimirlinha()
                id = int(leiaOpcao("\33[32mDigite o id da pessoa que você deseja remover:\33[m"))
                apagarDadosArquivo("dados.txt", id)
        elif op == 4:
            titulo("Saindo do Sistema... Até logo")
            sleep(1)
            break
        else:
            print("\33[31mERRO! Digite uma das opções do Menu\33[m")
            sleep(0.3)
    except KeyboardInterrupt:
            print("\n\33[31mO Usuario preferiu parar a execução do sistema!\33[m")
            titulo("Saindo do Sistema... Até logo")
            sleep(1)
            break
