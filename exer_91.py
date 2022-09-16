"""Crie um programa onde 4 jogadores joguem um dado e tanham resultados aleatorios. guarde esses resultadosem um dicionario. No final , coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior número no dado
"""
from operator import itemgetter
from random import randint
from time import sleep

print('-='*30)

jogadores = {'jogador 1':randint(1,6),'jogador 2': randint(1,6),'jogador 3': randint(1,6),'jogador 4':randint(1,6)}

for c,v in jogadores.items():
    print(f'{c} tirou {v} no dado.')
print('-='*30)
print('== RANKING DOS JOGADORES ==')

rank = []
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i,v in enumerate(rank):
    print(f'{i+1}º lugar {v[0]} com {v[1]}.')