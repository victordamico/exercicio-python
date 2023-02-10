"""Faça um programa  que leia um numero qualquer e mostre o seu fatorial."""

number = int(input('Digite um numero: '))
contador = number - 1 

print(number,'X',end=" ")
while contador > 0:
    print(contador, end=' ')
    print('X' if contador > 1 else ' = ', end=' ')
    number *=  contador
    contador -= 1 

print(f'{number}')
