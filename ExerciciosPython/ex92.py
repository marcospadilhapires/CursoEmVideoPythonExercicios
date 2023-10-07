from datetime import datetime

cadastro = {}
cadastro['Nome'] = str(input("Nome: "))
nasc = int(input("Ano de Nascimento: "))
cadastro['Idade']= datetime.now().year - nasc
cadastro['CTPS']= int(input("Carteira de Trabalho (0 para NÂO TEM): "))
if cadastro['CTPS'] != 0:
    cadastro['Contratacao'] = int(input("Ano da Contratação: "))
    cadastro['Salario'] = float(input("Salário: R$"))
    cadastro["idadeAposentadoria"] = (cadastro['Contratacao'] + 35) - nasc
print("-="*30)
for k,v in cadastro.items():
    print(f"   -{k} tem o valor {v}")

