"""Crie um programa que faça o computador jogar PEDRA PAPEL TESOURA com voce"""

from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL','TESOURA')
computer = randint(0,2)
print(computer)

print('=' * 10, 'PEDRA PAPEL TESOURA', '=' * 10)
print('ESCOLHA UMA OPÇÃO PARA JOGAR\n [ 0 ] PEDRA\n [ 1 ]PAPEL\n [ 2 ]TESOURA')

player = int(input('Escolhe PEDRA , PAPEL , TESOURA : '))



print(f'O computador jogou : {itens[computer]}')
print(f'Você escolheu {itens[player]}')


if computer == 0 and player == 1:
    print(' Voce Ganho')
    
elif player == 0 and computer == 1:
    print('O computador Ganhou ')

elif computer == 1 and player == 2:
    print('Voce Ganho')
    
elif computer == 2 and player == 1:
    print('O computador Ganhou')
else:
    print('Empate')