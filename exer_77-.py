'''
crie um programa que tenha uma tupla com varias palavras(não pode ter acentos). Depois disso, você deve mostrar, para cada palavra a sua vogais
'''
palavra = ('VEM','TOMA','E','LUGAR','AQUI','CINEMA','PARALELOGRAMA','POLIGONO','CANETA','CANETA','CELULAR','CARREGADOR','BALA','ANA')

for i in palavra:
    print(f'\nNa Palavra {i} temos', end=' ')
    for letra in i:
        if letra.upper() in 'AEIOU':
            print(letra,end=' ')
            

