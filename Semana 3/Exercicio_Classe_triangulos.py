# Defina a classe Triangulo cujo construtor recebe 3 valores inteiros correspondentes 
# aos lados a, b e c de um triângulo.
# A classe triângulo também deve possuir um método perimetro, que não recebe parâmetros 
# e devolve um valor inteiro correspondente ao perímetro do triângulo.

class Triangulo:
    
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = int(ladoA)
        self.ladoB = int(ladoB)
        self.ladoC = int(ladoC)

    def a(self):
        return self.ladoA

    def b(self):
        return self.ladoB

    def c(self):
        return self.ladoC

    def perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC

# Na classe triângulo, definida na Questão 1, escreva o metodo tipo_lado() que 
# devolve uma string dizendo se o triângulo é:
# isósceles (dois lados iguais)
# equilátero (todos os lados iguais)
# escaleno (todos os lados diferentes)
# Note que se o triângulo for equilátero, a função não deve devolver isóceles.

    def tipo_lado(self):
        if (self.ladoA == self.ladoB and self.ladoA == self.ladoC):
            return "equilátero"
        elif (self.ladoA == self.ladoB or self.ladoA == self.ladoC):
            return "isóceles"
        else:
            return "escaleno"

# Escreva, na classe Triangulo, o método retangulo() que devolve True se o triângulo for 
# retângulo, e False caso contrário.

    def retangulo(self):
        lados = []
        lados.append(self.ladoA)
        lados.append(self.ladoB)
        lados.append(self.ladoC)
        lados.sort()

        if (lados[0] ** 2 + lados[1] ** 2 == lados[2] ** 2):
            return True
        else:
            return False

# Ainda na classe Triangulo, escreva um método semelhantes(triangulo) que recebe 
# um objeto do tipo Triangulo como parâmetro e verifica se o triângulo atual é semelhante 
# ao triângulo passado como parâmetro. Caso positivo, o método deve devolver True. 
# Caso negativo, deve devolver False
# Um triângulo é semelhante a outro triângulo se a razão (divisão) entre os comprimentos 
# dos seus lados forem iguais.

    def semelhantes(self, trianguloEntrada):
        lados = []
        lados.append(self.ladoA)
        lados.append(self.ladoB)
        lados.append(self.ladoC)
        lados.sort()

        ladosEntrada = []
        ladosEntrada.append(trianguloEntrada.a())
        ladosEntrada.append(trianguloEntrada.b())        
        ladosEntrada.append(trianguloEntrada.c())
        ladosEntrada.sort()
        
        if (lados[0] / ladosEntrada[0] == lados[1] / ladosEntrada[1] == lados[2] / ladosEntrada[2]):
            return True
        else:
            return False
   

