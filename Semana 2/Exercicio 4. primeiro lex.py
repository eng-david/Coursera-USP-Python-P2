# Como pedido no segundo vídeo da semana, escreva a função primeiro_lex(lista) que recebe 
# uma lista de strings como parâmetro e devolve o primeiro string na ordem lexicográfica. 
# Neste exercício, considere letras maiúsculas e minúsculas.

def primeiro_lex(lista):    
    primeiroLex = lista[0]

    for item in lista:
        if item < primeiroLex:
            primeiroLex = item

    return primeiroLex

# input()
# lista = ['oĺá', 'A', 'a', 'casa']
# print(primeiro_lex(lista))