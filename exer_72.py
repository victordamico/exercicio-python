"""Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,de zero ate vinte
seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostrar por extenso"""

numbers =('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
          'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove')

while True:
    
    n = int(input('Digite um numero: '))
    if 0 <= n <= 20:
        break
    print('tente novamente')

print(f'voce digitou o número {numbers[n]}')