# Implemente a função ordena(lista), que recebe uma lista com números inteiros como parâmetro e 
# devolve esta lista ordenada em ordem crescente. Utilize o algoritmo selection sort.

def ordena(lista):
    size = len(lista)

    for i in range(size - 1):
        indiceMenor = i
        for j in range(i + 1, size):
            if lista[j] < lista[indiceMenor]:
                indiceMenor = j
        lista[i], lista[indiceMenor] = lista[indiceMenor], lista[i]

    return lista

# lista2 = ordena(lista)
# print(lista2)