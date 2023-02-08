"""Faça um programa que calcule a soma entre todos os numeros impares que são multiplo de tres de 1 a 500"""

soma = 0 
contador = 0
for time in range(1,500+1,2):
    if time % 3 == 0:
        contador += 1 
        soma += time 
    

print('contador',contador,'soma',soma)