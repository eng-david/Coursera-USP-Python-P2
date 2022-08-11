# Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e 
# devolve o índice correspondente à posição do elemento encontrado. Utilize o algoritmo de 
# busca sequencial. Nos casos em que o elemento buscado não existir na lista, a função deve 
# devolver o booleano False.

def busca(lista, elemento):
    size = len(lista)
    for i in range(size):
        if lista[i] == elemento:
            return i
    return False
