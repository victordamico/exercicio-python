"""Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa devera pertuntar se o usuario quer ou não continuar, No fianl, mostre 
A) quantas pessoas tem mais de 18 ano
B) quantos homens foram cadastrado
C) Quantas Mulheres tem menos de 20 anos"""

resposta = "S"
contador_idade = 0
contador_sexo = 0 
mulheres = 0 


print('-' * 30)
print('    CADASTRE UMA PESSOA')
print('-' * 30)

while resposta == 'S': 
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    if idade > 18:
        contador_idade += 1 
    elif sexo == 'M':
        contador_sexo += 1 
    if idade < 20 and sexo == 'F':
        mulheres += 1 
    print('-' * 30)
    resposta = input('Deseja continuar: ').strip().upper()

print(f'Foram cadastrada  {contador_idade} pessoas com mais de 18 anos: ')
print(f'Foram cadastrada  {contador_sexo} homens: ')
print(f'Foram cadastrada  {mulheres} mulheres com menos de 20 anos : ')



