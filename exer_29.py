"""Escreva um programa que leia a velocidade de um carro. se ele ultrapassar 80KM/H, mostre uma mensagem dizendo que ele foi multad. a multa vai custar R$ 7,00 por cada Km acima do limite """
velocity = int(input('Qual é a velocidade atual do caro ? '))

if velocity > 80: 
    subtraction = velocity - 80
    traffic_ticket = subtraction * 7
    print(f'\n\033[31mMULTA!!! sua velocidade passou de 80KM/H voce devera pagar uma multa de R${traffic_ticket}\033[m\n')

print('\033[32mTenha um bom dia\033[m\n')