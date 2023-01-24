"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quanto Dólares ela pode comprar"""

cash = float(input('Quanto dinheiro você tem R$:  '))
print(f'Com R$ {cash} você pode comprar U${(cash/5.2)}')