# Como proposto na primeira vídeo-aula da semana, escreva uma função imprime_matriz(matriz), 
# que recebe uma matriz como parâmetro e imprime a matriz, linha por linha. Note que NÃO se 
# deve imprimir espaços após o último elemento de cada linha!


def imprime_matriz (matriz):
    quantidadeLinhas = len(matriz)
    quantidadeColunas = len(matriz[0])

    for linha in range(quantidadeLinhas):
        for coluna in range(quantidadeColunas):
            print(matriz[linha][coluna], end="")
            if coluna < quantidadeColunas - 1: print(" ", end="")

        print("")

# imprime_matriz([[1,2],[3,9],[6,9]])