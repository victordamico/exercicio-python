"""Um professor quer sortear um dos seus quatro alunos para apagar o  quadro. faça um programa que ajude ele , lendo o nome deles e escrevendo o nome do escolhido"""

import random

student1 = input('Digite o nome do aluno: ')
student2 = input('Digite o nome do aluno: ')
student3 = input('Digite o nome do aluno: ')
student4 = input('Digite o nome do aluno: ')

liststudent = [student1,student2,student3,student4]

print(f'O aluno escolhido foi {random.choice(liststudent)}')