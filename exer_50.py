"""Desenvolva um programa que leia seis numeros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o"""

soma = 0
contador = 0
for time in range(1,6+1):
    number = int(input(f'Digite o valor numero {time} numero '))
    if number % 2 == 0 : 
        contador += 1
        soma += number
        

print(f'voce digitou {contador} pares e a soma é {soma}')