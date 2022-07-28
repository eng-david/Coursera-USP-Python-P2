# Duas matrizes são multiplicáveis se o número de colunas da primeira é igual ao número 
# de linhas da segunda. Escreva a função sao_multiplicaveis(m1, m2) que recebe duas matrizes 
# como parâmetro e devolve True se as matrizes forem multiplicavéis (na ordem dada) e False 
# caso contrário.

def sao_multiplicaveis (m1, m2):
    
    quantidadeColunasM1 = len(m1[0])

    quantidadeLinhasM2 = len(m2)

    if quantidadeColunasM1 == quantidadeLinhasM2:
        return True   
    else:
        return False
    
    
# m1 = [[1], [2], [3]]
# m2 = [[1, 2, 3]]
# print(sao_multiplicaveis(m1, m2))