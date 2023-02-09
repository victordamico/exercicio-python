"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido """

maior = 0 
menor = 0

for x in range(1,5+1):
    n = float(input(f'Pesso da {x}º pessoa: '))
    if x == 1:
        maior = n
        menor = n
    else: 
        if n > maior:
            maior = n
        if n < menor:
            menor = n
            
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
