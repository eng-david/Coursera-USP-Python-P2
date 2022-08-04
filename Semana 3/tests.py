import Exercicio_Classe_triangulos

while(1):
    a1 = input("a1: ")
    b1 = input("b1: ")
    c1 = input("c1: ")

    a2 = input("a2: ")
    b2 = input("b2: ")
    c2 = input("c2: ")

    t1 = Exercicio_Classe_triangulos.Triangulo(a1, b1, c1)
    t2 = Exercicio_Classe_triangulos.Triangulo(a2, b2, c2)

    # print(t1.a())
    # print(t1.b())
    # print(t1.c())
    print("")
    print("Perimetro T1: ", t1.perimetro())
    print("Tipo T1: ", t1.tipo_lado())
    print("Eh retangulo T1: ", t1.retangulo())

    print("")
    print("Perimetro T2: ", t2.perimetro())
    print("Tipo T2: ", t2.tipo_lado())
    print("Eh retangulo T2: ", t2.retangulo())

    print("")
    print(t1.semelhantes(t2))

