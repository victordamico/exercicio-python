"""Crie um programa que leia dois valores e mostre um menu como o ao lado na tela: seus programa devera realizar a operação solicitada em cada caso"""

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo valor: '))

operator = 0 

while operator != 5:
    print('\n[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVO NUMEROS\n[ 5 ] SAIR DO PROGRAMA  ')
    
    operator = int(input('Escolha uma Opção: '))
    
    if operator == 1: 
        print("_" * 30)
        print('SOMAR')
        soma = 0 
        soma = n1 + n2 
        print(f'{n1} + {n2} = {soma}')
        print("_" * 30)

    elif operator == 2: 
        print("_" * 30)
        print('MULTIPLICAR')
        mult = 0 
        mult = n1 * n2 
        print(f'{n1} X {n2} = {mult}')
        print("_" * 30)

    elif operator == 3: 
        print("_" * 30)
        print('MAIOR\n')
        if n1 > n2:
            print(f'{n1} é maior que  {n2} ')
        else:
            maior = n2
            print(f'{n2} é maior que  {n1} ')
        print("_" * 30)
        
    elif operator == 4: 
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo valor: '))
    elif operator == 5: 
        print('FIM DO PROCESSO')