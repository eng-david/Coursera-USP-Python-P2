# Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime 
# as dimensões da matriz recebida, no formato iXj.

def dimensoes(matriz):
    quantidadeLinhas = len(matriz)
    quantidadeColunas = len(matriz[0])
    
    print(str(quantidadeLinhas) + "X" + str(quantidadeColunas))

# m = [[1, 2, 3], [4, 5, 6]]
# dimensoes(m)