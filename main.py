# Prend en paramêtre un input avec une succession de underscore et de chiffre
import re

sudoku = input("Entrez le nom du fichier (avec son extension au format .txt) contenant la grille de sudoku à résoudre\n")
print("Format attendu dans le fichier:")
print("_729___3_\n__1__6_8_\n____4__6_\n96___41_8\n_487_5_96\n__56_8__3\n___4_2_1_\n85__6_327\n1__85____")

file = open(sudoku, "r")
file = file.read()


"""
    Vérifie le bon format du fichier dont le nom est passé en paramètre
"""


def check_data(file):
    # Supprime les retours à la ligne
    file = re.sub('[\n]', '', file)

    validCaracter = ['_', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    count = 0

    for char in file:
        if char not in validCaracter:
            print("Un caractère présent dans votre fichier est invalide")
            print("Format attendu dans le fichier:")
            print("_729___3_\n__1__6_8_\n____4__6_\n96___41_8\n_487_5_96\n__56_8__3\n___4_2_1_\n85__6_327\n1__85____")
            exit()
        else:
            count += 1

    if count == 81:
        return file
    else:
        print("Votre fichier contient trop de caractère le nombre de case doit être de 81 pour une grille de 9 * 9")


cleanFile = check_data(file)


"""
    Créer la matrice correspondante au plateau de jeu a partir de la string nettoyé
    Créer une fonction permettant de vérifier que la matrice respecte bien les règle du jeu
"""


def check_matrice(sudokuMatrice):
    pass

def create_matrice(cleanFile):

    check_matrice(sudokuMatrice)
    pass


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
