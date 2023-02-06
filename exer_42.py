"""Refaça o Desafio 035 dos triangulos, acrescentando o recursos de mostrar que tipo de triangulo sera formado
Equilatero: todos os lados iguais
isosceles: dois lados iguais
escaleno: todos os lados diferentes"""

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FOrmar um triangulo')

    if r1 == r2 == r3: 
        print('EQUILATERO!!!')
    elif r1 != r2 != r3:
        print('ESCALENO!!!')
    else:
        print('ISOSCELES!!')
else: 
    print('Os segmentos acima Não pode formar um triangulo')