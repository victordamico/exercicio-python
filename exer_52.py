"""Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo"""

number = int(input('Digite um nuemro: '))
contador = 0 
for x in range(1, number+1):
    if number % x == 0 : 
        print(f'\033[33m{x}\033[m',end=" ")
        contador += 1 
        
    else:
        print(f'\033[31m{x}\033[m', end=" ")
       
        
if contador == 2 or contador == 1 :
    print(f'O numero {number} foi divisivel por {contador} vezes\n por isso ele é Primo')
else:
    print(f'O numero {number} foi divisivel por {contador} vezes\n por isso ele NÃO  é Primo')
