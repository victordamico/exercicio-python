"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma area de 2m²"""

width = float(input('Largura:'))
height = float(input('Altura: '))
area = width * height

print(f'Sua parede tem a dimensão de {width}X{height} e sua área é de {area:.3}')
print(f'Para pintar essa parede, você precisará de {(area / 2 ) :.3}')