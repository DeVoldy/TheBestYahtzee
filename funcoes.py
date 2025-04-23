import random

def rolar_dados(n):
    lista_dados = []
    for i in range(n):
        lista_dados.append(random.randint(1,6))
    return lista_dados