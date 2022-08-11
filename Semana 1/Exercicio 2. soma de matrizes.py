# Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz que 
# represente sua soma caso as matrizes tenham dimensões iguais. Caso contrário, a função 
# deve devolver False.

def soma_matrizes (m1, m2):
    
    quantidadeLinhasM1 = len(m1)
    quantidadeColunasM1 = len(m1[0])

    quantidadeLinhasM2 = len(m2)
    quantidadeColunasM2 = len(m2[0])

    if quantidadeLinhasM1 == quantidadeLinhasM2 and quantidadeColunasM1 == quantidadeColunasM2: # se as matrizes forem do mesmo tamanho
        matrizRetorno = []

        for linha in range(quantidadeLinhasM1):
            lista = []

            for coluna in range(quantidadeColunasM1):
                soma = m1[linha][coluna] + m2[linha][coluna]
                lista.append(soma)

            matrizRetorno.append(lista)

        return matrizRetorno
    
    else:
        return False
    
    

# m1 = [[2],[1]]
# m2 = [[1,3],[6,7]]
# print(soma_matrizes(m1, m2))