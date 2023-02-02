"""Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual a base de conversãp 
[1] para binario
[2] para Octal
[3] para hexadecimal"""

number = int(input('Digite um numero: '))
options = int(input('Para converter para \nBinario digite [1]\nOctal Digite [2]\npara Hexadecimal digite [3] : '))

if options == 1:
    print(f'O numero {number} em Binario é: {bin(number)[2:]}')
elif options == 2:

    print(f'O numero {number} em Octal é: {oct(number)[2:]}')
elif options == 3: 
    print(f'O numero {number} em Hexadecimal  é: {hex(number)[2:]}')
else:
    print("ERRO voce não digitou nenhuma das opções disponiveis")

