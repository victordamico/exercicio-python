"""Crie um programa que leia o nome de uma cidade e diga se ela começa com ou não começa com ' Santos'"""

city = input('Digite  uma cidade que comece com Santos: ').strip()

print(city[0:6].title() == 'Santos')