"""Lendo o primeiro termo e a razão de um P.A, mostrando os 10 primeiro termos de progressão usando a estrutura whilw"""

print('Gerador de PA')
print('-=' * 12)

termo = int(input('Primeiro termo: '))

razao = int(input('Razão da PA : '))

contador = 0
while contador < 10:
    print(termo,'->',end=' ')
    termo += razao
    contador +=1

print('Fim\n', end=' ')