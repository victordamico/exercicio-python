"""Faça um programa que jogue par ou impar com o computador. O jogo so  sera interrompido quando o jogador PERDER, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo."""

from random import randint

pc = randint(0,10+1)

print(pc)

print('=' * 30)
print('VAMOS JOGAR IMPAR OU PAR')
print('=' * 30)

while True: 
    win = ' '
    value = ' '
    while win == value: 
        number = int(input('Digite um valor: '))
        value = input('Escolha Impar ou Par [I/P]:  ').upper().strip()


        if (number + pc) % 2 == 0 : 
            print(f'Você jogo {number} o computador escolheu {pc}. O total deu {number + pc} Par ')
            print('-=' * 30)
            win = 'P'
        else: 
            print(f'Você jogo {number} o computador escolheu {pc}. O total deu {number + pc} Impar')
            print('-=' * 30)
            win = 'I'
        if win == value:
            print('Voce Ganhou ')
            print('-=' * 30)
        else:
            print('Voce Perdeu')
            print('-=' * 30)
    break