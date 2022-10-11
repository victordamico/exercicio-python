"""Faça um programa que tenha uma função chamada Contador, seu programa tem que realizar três contagem atravez da função criada .

A) De 1 até 10, de 1 em 1 
B) De 10 até 0, de 2 em 2 
C) Uma contagem personalizada

"""
from time import sleep


def linhas():
    print('-='*30)

def Contador():
    linhas()
    """A) De 1 até 10, de 1 em 1 """
    print("Contagem de 1 até 10 de 1 em 1")
    for i in range(0,10+1):
        print(i, end="-", flush=True)
        sleep(0.1)
    print('Fim')
    linhas()
    sleep(0.1)
    """B) De 10 até 0, de 2 em 2 """
    print("Contagem de 10 até 0 de 2 em 2")
    sleep(0.1)
    for i in range(10,0-1,-2):
        print(i, end="-",  flush=True)
        sleep(0.1)
    sleep(0.1)
    print('Fim')
    linhas()
    """C) Uma contagem personalizada"""
    print('Agora é sua vez de persolizar a contagem')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    linhas()
    for i in range(inicio,fim,passo):
        print(i, end="-", flush=True)
        sleep(0.1)
    print('Fim')


Contador()









