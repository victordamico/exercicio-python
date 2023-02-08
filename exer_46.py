"""Faça um programa que mostre na tela uma contagem regressiva para estouro de fogo de artificio, indo de 10 ate 0, com uma pousa de 1 segundo entre eles."""

from time import sleep


for time in range(10,0-1,-1):
    print(time)
    sleep(1)
print('ACABOU')