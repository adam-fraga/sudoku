# Prend en paramêtre un input avec une succession de underscore et de chiffre
import re
import numpy as np
from numpy.core.numeric import False_

sudoku = input("Entrez le nom du fichier (avec son extension au format .txt) contenant la grille de sudoku à résoudre\n")
print("Format attendu dans le fichier:")
# print("_729___3_\n__1__6_8_\n____4__6_\n96___41_8\n_487_5_96\n__56_8__3\n___4_2_1_\n85__6_327\n1__85____")

file = open(sudoku, "r")
file = file.read()


"""
    Initialise la matrice correspondant au sudoku
"""


def create_matrice(file):
    file = re.split('\n', file)
    sudokuMatrice = []
    for row in file:
        sudokuMatrice.append(list(row))
    sudokuMatrice.pop()
    return sudokuMatrice


sudokuMatrice = create_matrice(file)


"""
    Créer une fonction permettant de vérifier que la matrice respecte bien les règles du jeu
"""


def check_matrice(sudokuMatrice):
    validChar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '_']

    for row in sudokuMatrice:
        for col in row:
            if col not in validChar:
                print("Votre fichier comporte des caractères invalides")
                return False
    return True


check_matrice(sudokuMatrice)

"""
   Récupère la ligne de la matrice correspondante à l'index courant et vérifie si le caractere existe en doublon
"""


def test_row(position: tuple, sudokuMatrice: list):
    # Récupère la ligne correspondant à l'index courant
    currentRow = sudokuMatrice[position[0]]
    # Stock la valeur a tester
    value = sudokuMatrice[position[0]][position[1]]
    # Initialise un compteur pour vérifier les doublon
    i = 0
    # Parcourt la ligne courante (récupéré sur la matrice)
    for x in currentRow:
        # Si Lors de l'itération sur la ligne courante un caractère match avec la valeur incrémente le compteur i
        if x == value:
            i += 1
    # Si i est strictement superieur à 1 alors la valeur existe en doublon sur la ligne renvoi False
    if i > 1:
        return False
    return True


"""
    Récupère la colonne de la matrice correspondante à l'index courant et vérifie si le caractere existe en doublon
"""


def test_col(position: tuple, sudokuMatrice: list):
    # Récupère la colonne courante
    currentCol = [col[position[1]] for col in sudokuMatrice]
    value = sudokuMatrice[position[0]][position[1]]
    # Vérifie que l'index courant n'éxiste pas en doublon sur la colonne de la matrice
    i = 0
    for x in currentCol:
        if x == value:
            i += 1
    if i > 1:
        return False
    return True


"""
    Récupère le bloc de sous jacent correspondant à l'index courant et vérifie si le caractere existe en doublon
"""


def test_block(position: tuple, sudokuMatrice: list):

    # Dictionnaire regroupant les différent bloc de la matrice
    dic = {"1st": [], "2nd": [], "3rd": [], "4th": [], "5th": [], "6th": [], "7th": [], "9th": []}
    i = 0
    
    # Append dans le tableau du dictionnaire correspondant en fonction de i
    for row in sudokuMatrice:
        for col in row:
            if i < 2 
            i += 1
    print(i)


test_block((2, 3), sudokuMatrice)


# # Aucun chiffre ne doit apparaite en doublon sur les colonnes
# # Récupère la colonne de l'indice courant et analyse tout les chiffres présent sur celle-ci
# def check_matrice(sudokuMatrice):
#     x = 0
#     y = 0

#     for row in sudokuMatrice:
#         for col in row:
#             if test_col((x, y), sudokuMatrice) and test_row((x, y, sudokuMatrice)) and test_block(x, y, sudokuMatrice):

#             else:
#                 check_matrice(sudokuMatrice)

#             print(x, y)
#             y += 1
#         y = 0
#         x += 1

#     pass

