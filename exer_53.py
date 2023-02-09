"""Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços"""

name = input('Digite um frase: ').upper()
name = name.replace(' ', '')

inverso = name[::-1]


print(f'O inverso de {name} é {inverso} ')
if name == inverso:
    print('A frase digitada é um palindromo')
else: 
    print('A frase digitada não é um palindromo')
