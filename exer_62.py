"""Melhore o Desafio 61 , perguntando para o usuario se lee quer mostrar mais alguns termos . o programa encerra quando ele disser quer quer mostarr 0 termos """

print('Gerador de PA')
print('-=' * 12)

termo = int(input('Primeiro termo: '))

razao = int(input('Razão da PA : '))

contador = 0

mais = 10
while mais != 0 :
    while contador < mais:
        print(termo,'->',end=' ')
        termo += razao
        contador +=1
    mais = int(input('\nVoce gostaria mais quantos termos : '))
    contador = 0

print('Fim\n', end=' ')