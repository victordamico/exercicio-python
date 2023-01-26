"""Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira."""

n = float(input('Digite um numero Real: '))

print(f'O valor digitado foi {n} e sua porção inteira é {int(n // 1 )}')