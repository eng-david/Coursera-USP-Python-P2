# Escreva a função ordenada(lista), que recebe uma lista com números inteiros como parâmetro e 
# devolve o booleano True se a lista estiver ordenada e False se a lista não estiver ordenada.

def ordenada(lista):   
    size = len(lista)

    iterations = 0
    for i in range(size - 1): # Testa Decrescente
        if lista[i] >= lista[i + 1]:             
            iterations += 1
            if iterations == size - 1: return True

    iterations = 0
    for i in range(size - 1):
        if lista[i] <= lista[i + 1]: # Testa Crescente         
            iterations += 1
            if iterations == size - 1: return True
    
    return False

# lista = [9,8,7,6,5,4,3,2,0]
# print(ordenada(lista))