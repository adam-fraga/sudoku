# Prend en paramêtre un input avec une succession de underscore et de chiffre
import re

sudoku = input("Entrez le nom du fichier (avec son extension au format .txt) contenant la grille de sudoku à résoudre\n")
print("Format attendu dans le fichier:")
# print("_729___3_\n__1__6_8_\n____4__6_\n96___41_8\n_487_5_96\n__56_8__3\n___4_2_1_\n85__6_327\n1__85____")

file = open(sudoku, "r")
file = file.read()


"""
    Initialise la matrice correspondant au sudoku
"""


def create_matrice(file):
    # Supprime les retours à la ligne
    file = re.split('\n', file)
    sudokuMatrice = []
    for row in file:
        sudokuMatrice.append([list(row)])

    print(sudokuMatrice)
    return sudokuMatrice


sudokuMatrice = create_matrice(file)


"""
    Créer une fonction permettant de vérifier que la matrice respecte bien les règles du jeu
"""


def check_matrice(sudokuMatrice):
    validChar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '_']

    for row in sudokuMatrice:
        for col in row:
            print("col", col)

    pass


check_matrice(sudokuMatrice)


"""
    Définir les methodes permettant la résolution du jeu
"""


# Aucun chiffre ne doit apparaite en doublon sur les colonnes
def check_col(cleanFile):
    pass


# Aucun chiffre ne doit apparaite en doublon sur les lignes
def check_row(cleanFile):
    pass


# Aucun chiffre ne doit apparaite en doublon sur les bloc de 3 * 3
def check_block(cleanFile):
    pass
