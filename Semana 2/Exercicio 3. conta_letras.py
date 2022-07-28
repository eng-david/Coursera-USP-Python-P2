# Escreva a função conta_letras(frase, contar="vogais"), que recebe como primeiro parâmetro 
# uma string contendo uma frase e como segundo parâmetro uma outra string. Este segundo 
# parâmetro deve ser opcional.
# Quando o segundo parâmetro for definido como "vogais", a função deve devolver o numero 
# de vogais presentes na frase. Quando ele for definido como "consoantes", a função deve 
# devolver o número de consoantes presentes na frase. Se este parâmetro não for passado 
# para a função, deve-se assumir o valor "vogais" para o parâmetro.

def conta_letras(frase, contar = "vogais"):    
    
    vogais = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117] # codigos ascii para vogais
    
    letrasAscii = [] # codigos ascii para todas as letras (menos a letra "a")
    for i in range (66, 91):
        letrasAscii.append(i)
    for i in range (98, 122):
        letrasAscii.append(i)      
    
    tamanhoFrase = len(frase)
    quantidadeVogais = 0
    quantidadeConsoantes = 0
    
    for i in range(tamanhoFrase):
        letra = frase[i]
        asciiCode = ord(letra)

        if asciiCode in vogais:
            quantidadeVogais += 1
        elif asciiCode in letrasAscii:
            quantidadeConsoantes += 1

    if contar == "vogais":
        return quantidadeVogais
    elif contar == "consoantes":
        return quantidadeConsoantes

# input()
# frase = 'programamos em python'
# print(conta_letras(frase, "consoantes"))