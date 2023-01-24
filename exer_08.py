"""Escreva um programa que leia uma valor em metros e o exiba convertido em centimetros ate milimetros"""

distance = float(input('Uma distancia em metros: '))

print(f'A medida de {distance} corresponde a \n{(distance / 1000)}km\n{distance / 100}hm\n{distance / 10}dam\n{distance * 10}dm\n{distance * 100}cm\n{(distance * 1000)}mm\n')