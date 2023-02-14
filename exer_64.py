"""Crie um programa que leia varios numeros inteiros pelo teclado, O programa so vai parar quando o ususario digitar o valor 999, que é a condição de parada. No final mostre quantos numeros foram digitados e qual foi a soma entre eles """

n = 0
contador = 0 
total = 0 

while True:
    while n != 999: 
        contador += 1
        total += n
        n = int(input('Digite um numero [999 para parar] : '))
    break
print(f'voce Digitou {contador - 1}   e a soma entre eles é {total} ')