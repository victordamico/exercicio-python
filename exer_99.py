"""Crie uma lista que tenha cada nome de 5 competidores e imprima em ordem aquele que deu mais volta na quadra, utilizando o sorted"""

competidores =[
    {"competidor": "Calor", "voltas": 4},
    {"competidor": "Calor", "voltas": 5},
    {"competidor": "Calor", "voltas": 1},
    {"competidor": "Calor", "voltas": 2},
    {"competidor": "Calor", "voltas": 9},
]

print(sorted(competidores, key= lambda competidor: competidor["voltas"] ))