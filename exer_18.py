"""Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo."""

import math 

angle = float(input('Digite o angulo que voce deseja: '))
sen = math.sin(math.radians(angle))

print(f'O angulo de {angle} tem o Seno de {sen :.2f}')
