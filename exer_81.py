#Crie um programa que vai ler Varios numeros e colocar em uma lista. Depois disso, motre 
#A)Quantos numeros foram digitados.
#B)A lista de valores, ordenada de forma decrecente.
#Se o valor 5 foi digitado e esta ou não na lista

lista = []
while True:
    lista.append(int(input('digite uma valor: ')))
    r = input('Deseja sair N/S: ')
    if r in 'Nn':
        break
print(f'fora digitados {len(lista)} elementos')
lista.sort()
print(f'lista em decrescente{lista.reverse()}')
if 5 in lista:
    print('o numero 5 esta na lista')
else:
    print('o numero 5 nao esta na lista ')

print(lista)
