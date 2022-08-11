# Escreva a função maiusculas(frase) que recebe uma frase (uma string) como parâmetro e devolve 
# uma string com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem.

def maiusculas(frase):
    tamanho = len(frase)
    letrasMaiusculas = ""

    for i in range(tamanho):
        letra = frase[i]
        asciiCode = ord(letra)
        
        if asciiCode >= 65 and asciiCode <= 90:
            letrasMaiusculas += letra        
        
    return letrasMaiusculas
    

# print(maiusculas(input()))