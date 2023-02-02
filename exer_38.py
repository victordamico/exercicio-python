"""Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:

O primeiro valor é maior 
O segundo valor é menor 
Não existe valor maior, os dois são iguais"""

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print(f'O primeiro é maior que o segundo {n1} > {n2}')

elif n2 > n1:
    print(f'O segundo é maior que o primeiro {n2} > {n1}')
else:
    print(f'Os dois são iguais')
