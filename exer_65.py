"""Crie um programa que leia varios numeros inteiros pelo teclado .No final da execução, mostre a media entre todos os valores e qual foi o maior e o menor valores lido. O programa deve perguntar ao ususario se ele qier ou não continuar a digitar os valores """

resposta = 'S'

contador = 0 

total = 0 

maior = 0

menor = 0 

while True:
    while resposta == 'S':
        number = int(input('Digite um numero: '))
        resposta = input('Voce gostaria de continuar [S/N]: ').upper().strip()
        contador += 1
        total += number 
        if contador == 1:
            maior = number
            menor = number
        elif number > maior:
            maior = number
        elif number < menor:
            menor = number
    break



print(f'Voce digitou {contador} e a média foi { total/contador}')
print(f'O maior valor foi {maior} e o menor foi {menor}')