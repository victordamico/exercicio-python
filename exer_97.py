
""" Criar um função que usar o **kwargs para retornar as cores favoritas de cada pessoa """



def color (**kwargs):
    for pessoa,cores in kwargs.items():
        print(f'A dor valorita de {pessoa.title()} é {cores.title()}')

color(marcos='verde',letiusia='rosa',rebeca='azul',felipe='amareLo',barbAra='Vermelho',Viutinho='LarAnja')