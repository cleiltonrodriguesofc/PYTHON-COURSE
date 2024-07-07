'''Faça um programa que tenha uma função notas() que pode receber várias 
notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas    
– A maior nota 
– A menor nota
– A média da turma
– A situação (opcional)'''
import statistics
def notas(*notas, sit=True):
    boletim = dict()
    boletim['total'] = len(notas)
    boletim['maior nota'] = max(notas)
    boletim['menor nota'] = min(notas)
    boletim['media'] = statistics.mean(notas)
    if sit:
        if boletim['media'] > 7:
            boletim['situação'] = 'BOA'
        elif boletim['media'] < 7:
            boletim['situação'] = 'RUIM'
    return boletim

resposta = notas(7, 9, 10, 2, 3, sit=True)
print(resposta)