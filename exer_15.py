"""Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade  de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e 0,15 por Km rodado"""

day = int(input('Quantos dias alugados: '))
km = float(input('Qunatos KM rodados: '))

print(f'O total a pagar é de R$ {(day * 60) + (km * 0.15)}')