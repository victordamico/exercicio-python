"""Escreva um programa qie pergunte o salario de um funcionario e calcule o valor do seu aumento .
para salarios superiores a R$ 1250, calcule um aumento de 10% para os inferiores ou igual , o aumento é de 15%"""

payment = float(input('Digite seu salario: '))

if payment > 1250:
    newpay =  payment * 1.1
else:
    newpay = payment * 1.15

print(f'quem ganhava R$ {payment} passa a ganhar {newpay:.2f}')