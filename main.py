import re
import copy as cp

sudoku = input("Entrez le nom du fichier (avec son extension au format .txt) contenant la grille de sudoku à résoudre\n")
print("Format attendu dans le fichier:")

print()
print()

print("_729___3_\n__1__6_8_\n____4__6_\n96___41_8\n_487_5_96\n__56_8__3\n___4_2_1_\n85__6_327\n1__85____")

print()
print()

file = open(sudoku, "r")

"""
    Class sudoku contient les attributs et méthodes relatives à la résolution du jeu
"""


class Sudoku:

    def __init__(self, file) -> None:

        self.stack = []
        self.result = None
        self.endgame = None
        self.strFile = file.read()
        self.sudokuMatrice = []
        self.currentRow = []
        self.currentCol = []
        self.currentBloc = None
        self.position = None

    """
        Initialise la matrice correspondante au sudoku
    """

    def set_matrice(self):
        file = re.split('\n', self.strFile)
        for row in file:
            self.sudokuMatrice.append(list(row))
        self.sudokuMatrice.pop()

    """
        Affiche la matrice du jeu
    """
    def print_matrice(self):
        for row in self.sudokuMatrice:
            print(row)

    """
        Fonction permettant de vérifier que la matrice respecte bien les règles du jeu
    """

    def check_matrice(self):
        validChar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '_']

        for row in self.sudokuMatrice:
            for col in row:
                if col not in validChar:
                    print("Votre fichier comporte des caractères invalides")
                    return False
        return True

    """
       Prend en paramètre la valeur (str) et un tuple (x, y)
       Récupère la ligne de la matrice correspondante à l'index courant et vérifie si le caractere existe en doublon
       Renvoi un booléen
    """

    def test_row(self, value: str, position: tuple):
        # Récupère la ligne correspondant à l'index courant
        self.currentRow = self.sudokuMatrice[position[0]]
        # Stock la valeur à tester
        # Initialise un compteur pour vérifier les doublons
        # Parcourt la ligne courante (récupéré sur la matrice)
        for x in self.currentRow:
            # Si Lors de l'itération sur la ligne courante un caractère match avec la valeur à inserer
            if x == value:
                return False
        return True

    """
        Prends en paramètre la valeur a tester (str) et la position sous forme de tuple (x, y)
        Récupère la colonne de la matrice correspondante à l'index courant et vérifie si le caractere existe en doublon
        Renvoi un booléen
    """

    def test_col(self, value: str, position: tuple):
        # Récupère la colonne courante
        self.currentCol = [col[position[1]] for col in self.sudokuMatrice]
        # Vérifie que l'index courant n'éxiste pas en doublon sur la colonne de la matrice
        for x in self.currentCol:
            if x == value:
                return False
        return True

    """
        Prends en parametre la valeur a tester (str), et la position sous forme de tuple (x, y)
        Définit temporairement la position courante de la matrice à True, en conservant une copie de la valeur initiale.
        Décompose la matrice en un dictionnaire de plusieurs tableaux ayant pour clé: 1st a 9th. CHaque Tableau
        représente un bloc du jeu (Square).
        Vérifie la présence de la valeur True en parsant les blocs un à un.
        Vérifie ensuite les doublons de la valeur passé en pramètre.
        Rétablit la valeur par défaut de la case courante.
    """

    def test_bloc(self, value: str, position: tuple):

        # Copie la valeur situé à la position courante dans une variable temporaire
        tmp = cp.copy(self.sudokuMatrice[position[0]][position[1]])
        # Affecte True à la position courante sur la matrice
        self.sudokuMatrice[position[0]][position[1]] = True

        # Dictionnaire regroupant les différents blocs de la matrice
        dic = {"1st": [], "2nd": [], "3rd": [], "4th": [], "5th": [], "6th": [], "7th": [], "8th": [], "9th": []}
        # Compteur
        i = 0

        # Pour chaque ligne de la matrice stoque les occurences de x a x rencontrés dans chaque bloc correspondant
        for row in self.sudokuMatrice:
            i += 1
            if i == 1 or i == 2 or i == 3:
                dic["1st"].append(row[:3])
                dic["2nd"].append(row[3:6])
                dic["3rd"].append(row[6:9])
            elif i == 4 or i == 5 or i == 6:
                dic["4th"].append(row[:3])
                dic["5th"].append(row[3:6])
                dic["6th"].append(row[6:9])
            elif i == 7 or i == 8 or i == 9:
                dic["7th"].append(row[:3])
                dic["8th"].append(row[3:6])
                dic["9th"].append(row[6:9])

        # Parcourt les différent tableaux pour vérifier si contient True (position courante) et set le bloc courant
        for key, val in dic.items():
            for item in val:
                if True in item:
                    self.currentBloc = key

        # Réinsert la aleur stocké temporairement dans la matrice
        self.sudokuMatrice[position[0]][position[1]] = tmp

        # Parcourt chaque élément du bloc courant pour vérifier si la valeur passé en parametre
        # est présente si oui c'est un doublon
        if self.currentBloc:
            for item in dic[self.currentBloc]:
                if value in item:
                    return False
        return True


"""
    Inititialise le jeu
"""
sudoku = Sudoku(file)
sudoku.set_matrice()

"""
    Affiche la matrice du jeu avant résolution
"""

print("Before Resolve")
sudoku.print_matrice()

"""
    Fonction de résolution du sudoku
"""


def sudoku_solver(sudoku: Sudoku):
    # Itère sur la matrice du jeu taille 9 * 9
    for x in range(9):
        for y in range(9):
            # Si case vide
            if sudoku.sudokuMatrice[x][y] == "_":
                # Pour valeur par case allant de 1 à 9 test chaque valeur
                for val in range(1, 10):
                    # Si valeur à position (x, y) non répétés dans row, col & block
                    if sudoku.test_bloc(str(val), (x, y)) and sudoku.test_row(str(val), (x, y)) and sudoku.test_col(str(val), (x, y)):
                        # Set val dans la matrice
                        sudoku.sudokuMatrice[x][y] = str(val)
                        # Affichage matrice après chaque insertion
                        sudoku.print_matrice()
                        print()
                        # Rappel la fonction
                        sudoku_solver(sudoku)
                # Pas de valeur trouvé pour la case courante la set de nouveau à "_"
                sudoku.sudokuMatrice[x][y] = "_"
                """
                    Retour dans la fonction parente celle-ci ne valant pas "_" la set également à "_"
                    etc... jusuqu'à la première case puis test la valeur suivante pour la première case.
                """
                return True
    # Sudoku résolue quitte le programme
    print("Résolution du sudoku terminée!")
    sudoku.print_matrice()
    exit()


"""
    Vérifie le bon format des caractères dans le fichier
"""
if sudoku.check_matrice():
    sudoku_solver(sudoku)

    print()
    print()

    print("After Resolve")
    for row in sudoku.result:
        print(row)

else:
    print("Votre fichiers contient des caractère non autorisés")
