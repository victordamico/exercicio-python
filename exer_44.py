"""Elabore um programa que calcule o valor a ser pago por um produto, considerado o seu preço normal e condições de pagamento:
- a vista dinheiro/cheque: 10% de desconto
a vista no cartão : 5% de desconto
em ate 2x no cartão: preço normal 
3x ou mais no cartão ; 20 % de juros """

print('=' * 11 ,'LOJINHA','=' * 11)

price = float(input('Preço das Compras: R$'))

print('FORMAS DE PAGAMENTO\n[ 1 ] á vista dinheiro\n[ 2 ] á vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão\n')

payment = int(input('Qual é a opção : '))

if payment == 1: 
    price *= 0.90
    print(f'Sua compra vai custar R${price} no final')
elif payment == 2: 
    price *= 0.95
    print(f'Sua compra vai custar R${price} no final')
elif payment == 3: 
    print(f'Sua compra vai custar R${price} no final')
else: 
    price *= 1.20
    print(f'Sua compra vai custar R${price} no final')
