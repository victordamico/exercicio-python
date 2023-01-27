"""Crie um programa que leia o nome complieto de uma pessoa e mostre:  
O nome com todas as Letras Maiusculo e Minuscula
Quantas letras ao tdo(sem cinsiderar espaços)
Quantas letras tem o primeiro nome"""

name = input('Digite se nome completo: ').strip()

print(f'O seu nome em maiúsculas é {name.upper()}')
print(f'O seu nome em maiúsculas é {name.lower()}')
print('O seu nome tem ao todos {} letras'.format(len(name) - name.count(' ')))
print('O seu primeiro nome tem {}'.format(name.find(' ')))


