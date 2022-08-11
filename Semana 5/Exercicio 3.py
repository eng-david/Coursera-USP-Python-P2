# Implemente a função insertion_sort(lista), que recebe uma lista com números inteiros como parâmetro e devolve 
# esta lista ordenada. Utilize o algoritmo insertion sort.

def insertion_sort(lista):
    for i in range(0, len(lista) - 1):
        chave = lista[i + 1]
        indice = i
       
        while indice >= 0 and chave < lista[indice]:
            lista[indice + 1] = lista[indice]
            indice = indice - 1
        
        lista[indice + 1] = chave

    return lista

lista = [11,12,2,4,3,6,5,7,8,9,10,1]
print(insertion_sort(lista))