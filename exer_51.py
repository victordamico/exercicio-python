"""Desenvolva ugressãom programa que leia o primeiro termo e a razão de uma PA no final, mostre os 10 primeiros termos dessas pro"""

print('=' * 10)

print('  10 TERMOS DE UMA PA  ')

print('=' * 10)

termo = int(input('Primeiro termo: '))

razao = int(input('Razão: '))

decimo = termo + (10 - 1 ) * razao

for x in range(termo,decimo + razao ,razao):
    print(x)