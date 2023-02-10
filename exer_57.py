"""Faça um programa que leia o sexo de uma pessoa, mas so aceita os Valores M ou F caso esteja errado, peça a digitação novamente ate ter um valor corretro """

sex = input('Informe seu sexo [M/F] : ').upper().strip()

while sex not in 'MF':
    print('\033[31mEsse valor esta incorreto digite novamente\033[m')
    sex = input('Informe seu sexo [M/F] : ').upper().strip()

print('Sexo amarzenado')