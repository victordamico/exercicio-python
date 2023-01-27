"""Faça um programa que leia  número de 0 9999 e mostre na tela cada um dos digitos separados."""

number = int(input('Informe um número: '))


thousands =  number // 1000
rest = number % 1000
hundred =  rest // 100
rest = number % 100
ten = rest // 10
rest = number % 10
unity = rest // 1





print(f'Analisando o numero {number}')
print(f'Unidade {unity }')
print(f'Dezena {ten}')
print(f'Centena: {hundred}')
print(f'Milhar : {thousands }')