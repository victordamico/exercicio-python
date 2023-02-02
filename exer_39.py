"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistado ao serviço militar se é hora de se alistar ou se ja passou do tempo do alistamento, Seu programa tambem devera mostrar io tempo que falta ou que passou do prazo """

from datetime import date


birth = int(input('Ano de nascimento: '))
year = date.today().year

print(f'Quem nasceu em {birth} tem {(year - birth)}')

if (year - birth) < 18 :
    print(f'Ainda falta {18 - (year - birth)} para o alistamento')
elif (year - birth) > 18:
    print(f'Você já deveria ter se alistado ha { (year - birth)- 18} ')
else:
    print('Voce tem que se alistar IMEDIATAMENTE')
