"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5%  de desconto."""

price = float(input('DIgite o preço do produto: '))

print('O preço atual com 5% de desconto  será de R${:.2f}'.format(price * 0.95))