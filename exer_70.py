"""Crie um programa que leia o nome e o preço de varios produtos. O programa devera perguntar se o usuario vai continuar. No final, mostre> 
A) Qual é o total gasto na compra 
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato. """

produto_menor = 0 
menor = 0
produto_maior = " "
total = 0 

print('-' * 30)
print('      LOJA SUPER BARATÃO    ')
print('-' * 30)

while True:
    name = " "
    price = 0 
    response = "S"
    contador = 0 
    while response == 'S':
        name = input('Nome do produto: ')
        price = float(input('Valor : '))
        response = input('Deseja continuar [S/N]: ').strip().upper()

        contador += 1 
        if contador == 1 :
            menor = price
            produto_menor = name
        elif price < menor: 
            menor= price
            produto_menor = name

            #aqui o menor não esta funcionando arrumar amanha
        if price > 1000:
            produto_maior = name
        
            

        total += price
    break
    
print(f'O total da compra ficou R${total}')
print(f'Temos {produto_maior} produto custando mais de R$ 1000')
print(f'O produto mais barato foi {produto_menor} e custa {menor}')

