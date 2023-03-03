"""Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,de zero ate vinte
seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostrar por extenso"""

numbers =('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
          'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove')

n = int(input('Digite um numero: '))
print(f'voce digitou o número {numbers[n]}')