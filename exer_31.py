"""Desenvolvaum programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem , cobrando R$0,50 por KM para viagens de ate 200km e R$0,45  para viagens maiores """

distance = float(input('digite a distancia em KM : '))

value = 0 

if distance <= 200:
    value = distance * 0.5
else:
    value = distance * 0.45

print(f' O preço da sua passagem ira ficar de R$ {value}')