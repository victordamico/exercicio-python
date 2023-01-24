"""Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário, com 15% de aumento"""

payment = float((input('Digite o salario: ')))
print(f'O salrio com um aumento de 15% ficará R${(payment * 1.15):.2f}')