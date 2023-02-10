"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
A media de idade do grupo 
Qual é o nome do homem mais velho 
Quantas mulheres tem menos de 20 anos."""

maior = 0 
person = ''
woman = 0
average = 0

for x in range(1,4+1):
    print(f'----- {x}º -----')
    name = input('Nome: ')
    age = int(input('Idade: '))
    sex = input('Sexo [M/F]: ').upper()
    
    average += age

    
    if sex == "F" and age < 20 :
        woman += 1 

    if age > maior and sex == "M":
        maior = age
        person = name


print(f'A media de idade do grupo é de {average/4} Anos')
print(f'O homem mais velho tem {maior} e se chama {person}')
print(f'Ao todo são {woman} mulheres com menos de 20 anos ')