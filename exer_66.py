"""Crie um programa que leia varios numeros inteiros pelo teclado. O programa sp vai para quando o usuuario digitar 999, que é a condição de parar . No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderendo o flag)"""



while True:
    total = 0 
    contador = 0 
    number =  int(input('Digite um valor (999 para parar): '))
    while number != 999:
        total += number
        contador += 1  
        number =  int(input('Digite um valor (999 para parar): '))
    break


print(f'A soma total dos {contador} valores foi de {total}')

