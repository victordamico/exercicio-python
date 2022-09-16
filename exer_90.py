''' façã um programa que leia nome e media de um aluno, guardando também a situaçãoem um dicionario. No final, mostre o conteúdo da estrutura na tela
'''

aluno = {}
aluno['nome'] = input('digite seu nome:')
aluno['media'] = int(input('Digite sua media: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] < 7 and aluno['media'] >= 6:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for c,v in aluno.items():
    print(f'- {c} é igual a {v}')


    