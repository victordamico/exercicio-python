"""Crie um programa qie leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores """

from datetime import date

menor = 0 
maior = 0 

for x in range(1,7+1):
    ano = int(input(f'Em que ano a {x} pessoa Nasceu:'))
    ano_atual = date.today().year
    value = ano_atual - ano
    if value < 18:
        menor += 1 
    else:
        maior += 1

print(f'Ao todo tivemos {maior} pesosa maiores de idade')
print(f'Ao todo tivemos {menor} pessoas menores de idade')