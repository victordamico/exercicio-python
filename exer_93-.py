''' Faça uma jogo, Pedra Papel e  Tesoura onde o usuario colocara um valor e o computador jogadora outro,
utilizando funções .
'''
from random import random

print('=-'*30)
print(" "*15,'Pedra Papel Tesoura')
print('=-'*30)

jogador = input('Escolha: Pedra Papel Tesoura:').capitalize()


def pedra_pepel_tesoura():
    computador = random
    if computador < 0.3:
        computador = 'Pedra'
    elif computador > 0.3 and computador < 0.6:
        computador = 'Papel'
    else:
        computador = 'Tesoura'
    return computador


print(pedra_pepel_tesoura())




