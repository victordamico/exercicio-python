"""faça uma tabuada usando o laço for """

x = int(input('Digite o valor da tabuada: '))
for tabuada in range(0,10+1):
    total = x * tabuada
    print(f'{tabuada} X {x} = {total}')