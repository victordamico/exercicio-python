"""Escreva um programa para provar o emprestimo bancario para a compra de uma casa. Pergunte o valor da casa, o salario , o salario do comprador e em quantos anos ela vai pagar.
A prestação mensal, não pode exceder 30% do salario ou então o emprestimo sera negado   """

value = float(input('Digite o valor do emprestimo: '))
payment = float(input('Digite o seu Salario: '))
year = int(input('Em quantos anos de financiamento: '))

month = year * 12

value = value / month
payment *= 0.3

if payment >= value:
    print(f'Para pegar esse valor em {year} anos a prestação ficara em R$ {payment}, emprestemo Aprovado ')
else:
    print(f'Para pegar esse valor em {year} anos a prestação ficara em R$ {payment} e esse valor passou de 30% do seu salario por esses motivos seu pedido foi Negado')
