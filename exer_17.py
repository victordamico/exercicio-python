"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento"""

import math


co = float(input('Comprimento do cateto Oposto: '))
ca = float(input('Comprimento do cateto Adjacente: '))
print(f'a Hipotenusa vai medir {(math.hypot(co,ca)):.2f}')