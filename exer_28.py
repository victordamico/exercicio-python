"""
Escreva um programa que faça o computador "pensar em um numero inteiro entre 0 e 5 e peça o usuario tentar adivinha qual é o numero escolhido pelo computador, o profeama devera escrever se o usuario venceu ou perdeu "
"""
from random import randint
from time import sleep

computer = randint(0,5)

print("\033[33m-=\033[m" * 30)
print(f'\033[36mVou pensar em um numero e voce tenta adivinhar\033[m')
print("\033[33m-=\033[m" * 30)


guess = int(input('Em que número eu pensei ? '))

print('\033[35mPROCESSANDO...\033[m')
sleep(3)

if  guess == computer: 
    print(f'\n\033[32mParabens voce ganhou!!\033[m\n')
else:
    print(f'\n\033[31mGanhei hahaha!!! Eu pensei no numero {computer} e não no {guess}\033[m\n')
