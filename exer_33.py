"""Faça um programa que leia tres númers e mostre qual é o maior e qual é o menor """

a = int(input('Digite o Primeiro numero: '))
b = int(input('Digite o Segundo numero: '))
c = int(input('Digite o Terceiro numero: '))

menor = a

if c < a and c < b :
    menor = c

if b < a and b < c:
    menor = b

maior = a



if c > a and c > b :
    maior = c

if b > a and b > c:
    maior = b


print(f'O maior numero é {maior}\n O menor numero é {menor}')