'''Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista no final,e mostre

A) Quantas pessoas foram cadastradas

B) Uma listagem com as pessoas mais pesadas

C) Uma listagem com as pessoas mais leves 
'''
lista = []
lista_temporaria = []
resposta = 'S'
maior = 0
menor = 0
nome_maior = ''
nome_menor = ''

while resposta == 'S':
    lista_temporaria.append(input('Nome: '))
    lista_temporaria.append(int(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = lista_temporaria[1]
    else:
        if lista_temporaria[1] > maior:
            maior = lista_temporaria[1]
        if lista_temporaria[1] < menor:
            menor = lista_temporaria[1]
    lista.append(lista_temporaria[:])
    lista_temporaria.clear()
    resposta = input('Deseja continuar [S/N]: ').upper()

for i in lista:
    if i[1] == maior:
          nome_maior = i[0]
    else:
        if i[1] == menor:
          nome_menor = i[0]   

print('-='*30)
print(f'Ao todo foram cadastrados {len(lista)} pessoas')
print(f'O maior peso foi de {maior}Kg, Que é de {nome_maior} ')
print(f'O menor peso foi de {menor}Kg, Que é de  {nome_menor} ')
print('-='*30)
print(lista)


