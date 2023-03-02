"""Crie um programa que simule o funcionamento de um caixa eletronico.No inicio,pergunte ao usuario qual sera o valor a ser sacado (numro inteiro ) e o programa vai informar quantas cedulas de cada valor serão engues

OBS: o caixa so tem cedulas de 50,20,10 e 1 """

print('=' * 30)
print(' ' * 10, 'Bando CEV',' ' * 10 )
print('=' * 30)

value = int(input('Que valor você quer sacar: R$'))

cedula = 0 
while  value > 0 :
      #cedula de R$50 
    if value // 50:
        cedula = value // 50
        print(f'total de {cedula} cedula de R$ 50')
        value %= 50
    #cedula de R$20 
    if value // 20:
        cedula = value // 20
        print(f'total de {cedula} cedula de R$ 20')
        value %= 20
    #cedula de R$10 
    if value // 10:
        cedula = value // 10
        print(f'total de {cedula} cedula de R$ 10')
        value %= 10
    #cedula de R$1
    if value // 1:
        cedula = value // 1
        print(f'total de {cedula} cedula de R$ 1')
        value %= 1
        

    break
