"""Crie um programa que faça o computador jogar PEDRA PAPEL TESOURA com voce"""

from random import randint
from time import sleep

computer = randint(1,2,3)
print(computer)

print('=' * 10, 'PEDRA PAPEL TESOURA', '=' * 10)
print('ESCOLHA UMA OPÇÃO PARA JOGAR\n [ 0 ] PEDRA\n [ 1 ]PAPEL\n[ 2 ]TESOURA')
