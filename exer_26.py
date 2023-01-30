"""Faça um  programa que leia uma frase pelo  teclado e mostre : 
Quantas vezes aparece a letra  'A' 
Em que posição ela aparece a primeira vez
em que posição ela aparece a ultima vez """

name = input('Digite uma frase:  ').upper()

print(f' letra "A" aparece  {name.count("A")} vezes')
print(f'A primeira letra "A" aparece na posição {name.find("A")+1}')
print(f'A ultima letra "A" aparece na posição {name.rfind("A")+1}')


