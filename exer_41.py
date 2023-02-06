"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: 
ate 9 anos : mirim
ate 14 anos : infantil
ate 19 nos : junior 
ate 25 anos: senior
acima de 25 : master"""



from datetime import date

ano = int(input('Ano de Nascimento: '))

current_age = (date.today().year - ano )

print(f'O atleta tem : {current_age} anos.')

if current_age <= 9:
    print('Classificação: Mirim')
elif current_age > 9 and  current_age <= 14  :
    print('Classificação: Infantil')

elif current_age > 14 and  current_age <= 19  :
    print('Classificação: Junior')
elif current_age > 19 and  current_age <= 25  :
    print('Classificação: Senior')
elif current_age > 25  :
    print('Classificação: Master')