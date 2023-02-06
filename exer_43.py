"""Desenvolva uma logica que leia o peso e altura de uma pessoa calcule seu IMC e mostre seu status, de acoro com a tabela abaixo:
-Abaixo de 18,5:Abaixo do peso             -25 ate 30: sobrepeso
-Entre 18.5 e 25: peso ideal               - 30 ate 40: Obesidade
- Acima de 40: obesidade morbida """


weight = float(input('Qual é sei peso? (Kg) '))

height = float(input('Qual é sia altura? (M)'))

imc = weight / (height ** 2)

print(f'O IMC dessa pessoa é de {imc}')
if imc < 18.5 :
    print('Abaixo do pesso')
elif imc >= 18.5  and imc < 25:
    print('Peso ideal')
elif imc >= 25  and imc < 30:
    print('Sobre peso')
elif imc >= 30.5  and imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')