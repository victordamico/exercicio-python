"""Escreva um programa que leia um numero N inteiro quaquer e mostre na tela os N primeiro elementos de uma sequencia de Fibonacci"""

print('-' * 12) 
print('Sequencoia de Fibonacci')
print('-' * 12) 

termo = int(input('Quantos termos voce quer mostrar: '))

contador = 0
n1 = 0
n2 = 1
resultado = 0
print(n1, '->', end=' ')
print(n2, '->', end=' ')


while contador < termo:
    resultado = n1 + n2
    print(resultado, '->', end=' ')
    contador += 1 
    n1 = n2
    n2 = resultado
    