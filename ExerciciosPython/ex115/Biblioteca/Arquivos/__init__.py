from time import sleep
import os

lista = []
def adicionardados(txt,nome, idade):
    with open(txt,"a") as arquivo:
        print("Registrando...")
        arquivo.write(f"{nome:<35}{str(idade) + ' anos':>8}\n")
        sleep(1)
        print("Pessoa cadastrada com sucesso!")
        sleep(1)


def lerArquivo(txt):
    try:
        with open(txt,"r") as arquivo:
            pessoas = arquivo.readlines()
        for c,pessoa in enumerate(pessoas):
            pessoa = pessoa.replace("\n","")
            print(f"{c} - {pessoa}")
    except FileNotFoundError:
        print("Não existe pessoas cadastradas!")
        return False
    else:
        return True

def apagarDadosArquivo(txt,dado):
    with open(txt,"r") as arquivoleitura:
        pessoas = arquivoleitura.readlines()
        c = 0
        with open(txt,"w") as arquivomodificar:
            for pessoa in pessoas:
                if c != dado:
                    arquivomodificar.write(pessoa)
                c+=1
    arquivoexcluir = open(txt)
    if arquivoexcluir.read() == "":
        arquivoexcluir.close()
        removerArquivo(txt)
    print("Pessoa apagada com sucesso")


def removerArquivo(txt):
    os.remove(txt)

