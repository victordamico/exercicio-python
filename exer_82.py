""" Crie um programa que vai ler varios numero e colocar em uma lista. Depois disso, crie duas lista extra que vão contar apenas os valores pares e os valores impares digitados,respectivamente.Ao final mostre o conteudo das Três lista geradas
"""
lista = []
lp = []
li = []

while True:
    lista.append(int(input('digite um valor: ')))
    resposta = input('Deseja Contiar N/S: ')
    if resposta in 'nN':
        break
for i in lista:
    if i % 2 == 0: 
        lp.append(i)
    else: 
        li.append(i)
        
print(f'A lista completa é {lista}')
print(f'A lista de pares completa é {lp}')
print(f'A lista de impares completa é {li}')

        



