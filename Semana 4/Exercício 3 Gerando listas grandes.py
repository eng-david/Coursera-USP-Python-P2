# Escreva a função lista_grande(n), que recebe como parâmetro um número inteiro n e devolve 
# uma lista contendo n números inteiros aleatórios.

from random import randint


def lista_grande(n):
    lista = []
    for i in range(n):
        lista.append(randint(-1000, 1000))
    return lista

# lista = lista_grande(50)
# print(lista)


