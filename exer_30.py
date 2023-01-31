"""Faça um programa que diga se o numero digitado é impar ou é par """
number = int(input('Digite um numero: '))

if number % 2 == 0: 
    print(f'O numero {number} é PAR')
else:
    print(f'O numero {number} é IMPAR')
