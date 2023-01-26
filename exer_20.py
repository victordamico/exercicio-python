"""O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. faça um programa que leia o nome dos quatro aludos e mostre a ordem"""

import random

student1 = input('Primeiro aluno: ').title()
student2 = input('Segundo aluno: ').title()
student3 = input('Terceiro aluno: ').title()
student4 = input('Quarto aluno: ').title()

liststudent = [student1,student2,student3,student4]
random.shuffle(liststudent)

print(f'A ordem de apresentação sera {(liststudent)}')