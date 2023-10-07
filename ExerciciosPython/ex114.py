from urllib import request
try:
    site = request.urlopen("http://pudim.com.br/")
except urllib.error.URLError:
    print("Não é possivel acessar o site http://pudim.com.br/")
else:
    print("A conexão com o site http://pudim.com.br/ foi feita com sucesso!")
    print(site.read())

