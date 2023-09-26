import numpy as num
import math
import matplotlib.pyplot as plot
import Lib2matrces as lvs

def calculo(mat, vect, click):
    if click == 0:
        return vect
    elif click == 1:
        return lvs.sobrevector(mat, vect)
    else:
        return lvs.sobrevector(mat, calculo(mat, vect, click - 1))

def mod_cuadrado(c):
    return round(c.real * 2 + c.imag * 2, 2)

#Retos del capitulo 3
# reto 3.1.1
def canicas(mat, vect, click):
    if len(mat) != len(mat[0]):
        final = "Tamaño incorrecto de matriz"
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] != 0 or mat[i][j] != 1:
                final = "Matriz no booleana"
                break
    else:
        final = calculo(mat, vect, click)
    return final

# reto 3.2.1
def fracciones(mat, vect, click):
    if len(mat) != len(mat[0]):
        final = "tamaño incorrecto de matriz"
    for i in range(len(mat)):
        suma = 0
        for j in range(len(mat[0])):
            suma += mat[i][j]
        if suma != 1:
            final = "Matriz no doblemente estocástica"
            break
    for i in range(len(lvs.transpuesta(mat))):
        suma = 0
        for j in range(len(lvs.transpuesta(mat)[0])):
            suma += mat[i][j]
        if suma != 1:
            final = "Matriz no doblemente estocástica"
            break
    else:
        final = calculo(mat, vect, click)
        final = [round(x, 2) for x in final]
    return final

# reto 3.2.2
def exp_rendijas(white, rendija):
    mat = [[0 for x in range(white + rendija + 1)] for x in range(white + rendija + 1)]
    vez = white // rendija if white % 2 == 0 else (white + 1) // (rendija)
    j = rendija + 1
    for k in range(1, rendija + 1):
        mat[k][0] = round(1 / rendija, 2)
        for i in range(j, j + vez):
            mat[i][k] = round(1 / vez, 2)
        j += vez - 1
        for l in range(len(mat) - white, len(mat)):
            mat[l][l] = 1
    vect = [0 for x in range(len(mat))]
    vect[0] = 1
    mat1 = lvs.prod_de_matz(mat, mat)
    vect = lvs.sobrevector(mat1, vect)
    return mat, vect

# reto 3.3.1
def complex(mat, vect, click):
    if len(mat) != len(mat[0]):
        final = "Tamaño incorrecto de matriz"
    for i in range(len(mat)):
        suma = 0
        for j in range(len(mat[0])):
            suma += mod_cuadrado(mat[i][j])
        if suma != 1:
            final = "Matriz no doblemente estocástica"
            break
    for i in range(len(lvs.transpuesta(mat))):
        suma = 0
        for j in range(len(lvs.transpuesta(mat)[0])):
            suma += mod_cuadrado(mat[i][j])
        if suma != 1:
            final = "Matriz no doblemente estocástica"
            break
    else:
        final = calculo(mat, vect, click)
    return final

# reto 3.3.2
def exp_rendija_cuantica(mat):
    vecto = [0 for x in range(len(mat))]
    vecto[0] = 1
    mat = lvs.prod_de_matz(mat, mat)
    vecto = lvs.sobrevector(mat, vecto)
    return vecto

def grafica(vecto):
    dato = len(vecto)
    x = num.array([x for x in range(dato)])
    y = num.array([round(vecto[x] * 100, 2) for x in range(dato)])
    plot.bar(x, y, color='b', align='center')
    plot.title('Probabilidad del vector en %')
    plot.savefig("Caso.jpg")
    plot.show()
def main()
    print(canicas([[0, 0, 1], [1, 0, 0], [0, 1, 0]], [3, 6, 9], 5))
    print(fracciones([[1 / 3, 2 / 3, 0], [2 / 3, 1 / 3, 0], [0, 0, 1]], [1, 0, 0], 3))
    print(exp_rendijas(5, 2))
    print(complex([[1 / math.sqrt(2), 1 / math.sqrt(2), 0], [-1j / math.sqrt(2), 1j / math.sqrt(2), 0], [0, 0, 1j]],
                  [1 / math.sqrt(3), 2j / math.sqrt(15), math.sqrt(2 / 5)], 1))
    print(grafica(fracciones([[1 / 3, 2 / 3, 0], [2 / 3, 1 / 3, 0], [0, 0, 1]], [1, 0, 0], 1)))
main()