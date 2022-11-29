"""Crie uma lista que tenha cada nome de 5 competidores e imprima em ordem aquele que deu mais volta na quadra, utilizando o sorted"""

competidores =[
    {"competidor": "Calor", "voltas": 4},
    {"competidor": "Victor", "voltas": 5},
    {"competidor": "Henrique", "voltas": 1},
    {"competidor": "Rebeca", "voltas": 2},
    {"competidor": "Celio", "voltas": 9},
]

print(max(competidores, key= lambda competidor: competidor["competidor"] ))
print(min(competidores, key= lambda competidor: competidor["competidor"] ))
#
