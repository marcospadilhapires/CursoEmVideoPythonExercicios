def notas(*notas, sit=False):
    """
    -> Verificar notas dos alunos e retornar um dicionário com as informações:
        -Quantidade de notas
        -A maior nota
        -A menor nota
        -A média
        -A situação(opcional)

    :param notas: uma ou mais notas do aluno.
    :param sit(opcional): True para mostrar a sintuação do aluno.
    :return: Dicionário com as informações das notas.
    """
    aluno = dict()
    # aluno['Quantidade de notas'] = 0
    # for c, nota in enumerate(notas):
    #     aluno['Quantidade de notas'] += 1
    #     if c == 0:
    #         aluno['Maior nota'] = nota
    #         aluno['Menor nota'] = nota
    #     else:
    #         if nota > aluno['Maior nota']:
    #             aluno['Maior nota'] = nota
    #         elif nota < aluno['Menor nota']:
    #             aluno['Menor nota'] = nota
    # aluno['Média'] = sum(notas) / aluno['Quantidade de notas']

    aluno['Quantidade de notas'] = len(notas)
    aluno['Maior nota'] = max(notas)
    aluno['Menor nota'] = min(notas)
    aluno['Média'] = sum(notas)/ len(notas)

    if sit:
        if aluno['Média'] < 5:
            aluno['Sintuação'] = 'Reprovado'
        elif 5 <= aluno['Média'] < 7:
            aluno['Sintuação'] = 'Recuperação'
        else:
            aluno['Sintuação'] = 'Aprovado'
    return aluno


# Programa Principal
r = notas(5.5,2.4,10,10)
print(r)
help(notas)
