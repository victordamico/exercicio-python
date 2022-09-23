#84) Faça um programa que leia nome e peso de varias pessoa, guardando tudo em uma lista. No final,Mostre:
#A) Quantas pessoas foram cadastradas
#B)Uma listagem com as pessoas mais pesadas
#C) Uma lista com as pessoas mais leves

lista0 = []
lista1 = []
maior = menor = 0
while True:
    lista0.append(input('Nome: '))
    lista0.append(float(input('Peso: ')))
    if len(lista1) == 0:
        maior = menor = lista0[1]      #[0] nome  [1] peso
    else:
        if lista0[1] > maior :   #se lista na posição 1 for maior que maior = 0 
            maior = lista0 [1]    #maior vai receber o valor da posição 1 
        if lista0[1] < menor:
            menor = lista0[1]

    lista1.append(lista0 [:]) 
    lista0.clear()
    resp = input('Deseja continuar [S/N]: ').upper()
    if resp == 'N':
        break

print(f'os dados que você digitou foram {lista1}')
print(f'o numero de pessoas cadastrada foram : {len(lista0)} pessoas ')
print(f'o maior peso cadastrado foi: {maior} KG ', end='')
for i in lista1:
    if i[1] == maior:
        print(f'Peso de {i[0]}')
print()

print(f'o menor peso cadastrado foi: {menor} KG ', end='')
for i in lista1:
    if i[1] == menor:
        print(f'Peso de {i[0]}')
print()
