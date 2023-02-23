"""Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. O programa sera interrompido quando o numero solicitado for negativo"""

while True: 
    number = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30 ) 

    if number < 0:
        print('Digite um numeor positivo ')
        break
    
    for contador in range(0,10 + 1 ):
        print(f'{number} X {contador} = {number * contador}')
