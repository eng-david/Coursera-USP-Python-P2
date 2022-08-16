# Implemente a função bubble_sort(lista), que recebe uma lista com números inteiros como parâmetro e devolve esta 
# lista ordenada. Utilize o algoritmo bubble sort.
# Além de devolver uma lista ordenada, ao longo do processamento sua função deve imprimir o estado atual da lista 
# toda vez que fizer uma alteração em seus elementos.

def bubble_sort(lista):
    ultimo = len(lista) - 1
    
    for i in range(ultimo, 0, -1):
        foiModificado = False
        
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j+1], lista[j] = lista[j], lista[j+1]
                foiModificado = True
                print(lista)
        
        if not foiModificado: 
            return lista

    return lista

# lista = [2,4,3,6,5,1,7,8,9,10]
# print(bubble_sort(lista))