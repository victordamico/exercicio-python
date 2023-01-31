"""Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO"""

from datetime import date

ano = int(input('Que ano quer analisar ? coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 :
    print(f'O ano {ano} é BISSEXTO ')
else:
    print(f'O ano {ano} Não é BISSEXTO ')
