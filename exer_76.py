#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia. No final, mostre uma listagem de preço, organizando os dados em forma tabular.
listagem = ('Caderno',15.80,'Folha',3,'Estojo',25,'Borracha',2,'Transferidor',4.20,'Compasso',9.99,'livro',50)

print('-'*50)
print(' '*17,'LISTAGEM DE PREÇOS',' '*17)
print('-'*50)
for i in range(0,len(listagem)+1):
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end='') #< alinhado a esquerda
    else:
        print(f'R${listagem[i]:.>1}')# > alinha para direita
        
print('novo teste')

