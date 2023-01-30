
"""Faça um programa que leia o nome completo de uma pessoa. mostre em seguida o primeiro e o ultimo nome dela """

name = input("DIgite seu nome completo: ").strip()

n = name.split()

print(f'Prazer em conhecer {name.title()}')
print(f'O seu primeiro nome é {(n[0]).title()}')
print(f'O seu ultimo nome é {(n[-1]).title()}')
