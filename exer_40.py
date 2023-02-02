"""Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida:
Media abaixo de 5.00: REPROVADO
media entre 5.0 e 6.9: RECUPERAÇAO
media 7 ou superior: APROVADO"""

note = float(input('Digite sua primeira nota: '))
note2 = float(input('Digite sua seunda nota: '))

if ((note + note2)/2) < 5 :
    print('REPROVADO')
elif ((note + note2)/2) >= 5 and ((note + note2)/2) <=6.9 :
    print('RECUPERAÇÃO')
else:
    print('APROVADO')