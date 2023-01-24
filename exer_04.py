"""Faça um programa que leia algo  pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele"""

some = input("Digite algo: ")

print(f'O tipo desse valor é {type(some)}')
print(f'Só tem espaço ? {some.isspace()}')
print(f'É um número ? {some.isnumeric()}')
print(f'É alfabetico? {some.isalpha()}')
print(f'É um alfanumerico? {some.isalnum()}')
print(f'É um maiúsculas ?{some.isupper()}')
print(f'É um minúsculas ?{some.islower()}')
print(f'É um capitalizada ?{some.istitle()}')







