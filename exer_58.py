"""Faça um programa onde o computador vai "pensar" em um numero entre 0 e 10. So que agora o jogador vai tentar adivinhar ate, mostrando no final quantos palpites foram nescessario para vencer """

from random import uniform

secret_number = int(uniform(0, 10+1))


number = int(input('Diga seu palpite: '))


while number != secret_number:
    print('\033[31mEsse não é o valor correto tente novamente\033[m')
    number = int(input('Diga seu palpite: '))

print('\n\033[32mPabens voce acertou!!!\033[m\n')