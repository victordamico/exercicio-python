"""Crie um programa que leia o nome e o preço de varios produtos. O programa devera perguntar se o usuario vai continuar. No final, mostre> 
A) Qual é o total gasto na compra 
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato. """

lowest_price = 0 
lowest_price_value = 0
high_price = " "
total = 0 

print('-' * 30)
print('      LOJA SUPER BARATÃO    ')
print('-' * 30)

while True:
    name = " "
    price = 0 
    response = "S"
    while response == 'S':
        name = input('Nome do produto: ')
        price = float(input('Valor : '))
        response = input('Deseja continuar [S/N]: ').strip().upper()
        if lowest_price_value < price :
            lowest_price_value= price
            lowest_price = name
            #aqui o menor não esta funcionando arrumar amanha
        if price > 1000:
            high_price = name
            

        total += price
    break
    
print(f'O total da compra ficou R${total}')
print(f'Temos {high_price} produto custando mais de R$ 1000')
print(f'O produto mais barato foi {lowest_price} e custa {lowest_price_value}')

