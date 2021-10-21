# Prend en paramêtre un input avec une succession de underscore et de chiffre
import re
import copy as cp

sudoku = input("Entrez le nom du fichier (avec son extension au format .txt) contenant la grille de sudoku à résoudre\n")
print("Format attendu dans le fichier:")
print("_729___3_\n__1__6_8_\n____4__6_\n96___41_8\n_487_5_96\n__56_8__3\n___4_2_1_\n85__6_327\n1__85____")
file = open(sudoku, "r")


class Sudoku:

    def __init__(self, file) -> None:

        self.strFile = file.read()
        self.sudokuMatrice = []
        self.currentRow = []
        self.currentCol = []
        self.currentBloc = None
        self.position = []
        self.count = 0

    """
        Initialise la matrice correspondante au sudoku
    """

    def set_matrice(self):
        file = re.split('\n', self.strFile)
        for row in file:
            self.sudokuMatrice.append(list(row))
        self.sudokuMatrice.pop()

    """
        Créer une fonction permettant de vérifier que la matrice respecte bien les règles du jeu
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
       Récupère la ligne de la matrice correspondante à l'index courant et vérifie si le caractere existe en doublon
    """

    def test_row(self):
        # Récupère la ligne correspondant à l'index courant
        self.currentRow = self.sudokuMatrice[self.position[0]]
        # Stock la valeur a tester
        value = self.sudokuMatrice[self.position[0]][self.position[1]]
        # Initialise un compteur pour vérifier les doublon
        i = 0
        # Parcourt la ligne courante (récupéré sur la matrice)
        for x in self.currentRow:
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

    def test_col(self):
        # Récupère la colonne courante
        self.currentCol = [col[self.position[1]] for col in self.sudokuMatrice]
        value = self.sudokuMatrice[self.position[0]][self.position[1]]
        # Vérifie que l'index courant n'éxiste pas en doublon sur la colonne de la matrice
        i = 0
        for x in self.currentCol:
            if x == value:
                i += 1
        if i > 1:
            return False
        return True

    """
        Définit temporairement la position courante de la matrice à True, en conservant une copie de la valeur initiale.
        (passée en paramètre).
        Décompose la matrice en un dictionnaire de plusieurs tableaux ayant pour clé: 1st a 9th. CHaque Tableau
        représente un bloc du jeu.
        Vérifie la présence de la valeur True en parsant les blocs un à un.
        Vérifie ensuite les doublons de la valeur conserver en copie dans ce même bloc avant de redéfinir celle-ci
        sur la matrice.
    """

    def test_bloc(self):

        tmp = cp.copy(self.sudokuMatrice[self.position[0]][self.position[1]])
        self.sudokuMatrice[self.position[0]][self.position[1]] = True

        # Dictionnaire regroupant les différents bloc de la matrice
        dic = {"1st": [], "2nd": [], "3rd": [], "4th": [], "5th": [], "6th": [], "7th": [], "8th": [], "9th": []}
        # Compteur
        i = 0

        # Pour chaque ligne de la matrice stock les occurences de x a x rencontré dans chaque bloc correspondant
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
        for key, value in dic.items():
            for item in value:
                if True in item:
                    self.currentBloc = key

        # Réinsert la valeur initiale dans la matrice
        self.sudokuMatrice[self.position[0]][self.position[1]] = tmp

        # Parcourt chaque élément du bloc courant pour vérifier si le caractère est présent si oui c'est un doublon
        if self.currentBloc:
            for item in dic[self.currentBloc]:
                if tmp in item:
                    return False
        return True


sudo = Sudoku(file)
sudo.set_matrice()

print("BEFORE RESOLVE")
for row in sudo.sudokuMatrice:
    print(row)

"""
    Fonction récursive de résolution du sudoku
"""


def sudoku_resolver(sudoku: Sudoku):
    # Initialise les variables de position x et y et un compteur i
    x = 0
    y = 0
    # Caractère à inserer pour completer le jeu
    numbs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Itère sur la matrice du jeu
    for row in sudo.sudokuMatrice:
        for col in row:
            # Stock les positions x et y auto incrémenté dans l'attribut position
            sudoku.position = (x, y)
            # Si le caractère est un "_" insert un nombre
            if sudoku.sudokuMatrice[sudoku.position[0]][sudoku.position[1]] == "_":
                sudoku.sudokuMatrice[sudoku.position[0]][sudoku.position[1]] = numbs[sudoku.count]
                if sudoku.test_col() and sudo.test_row() and sudo.test_bloc():
                    for row in sudo.sudokuMatrice:
                        print(row)
                    print()
                else:
                    sudoku.sudokuMatrice[sudoku.position[0]][sudoku.position[1]] = "_"
                    sudoku.count += 1
                    print("compteur", sudoku.count)
                    if sudoku.count > 8:
                        sudoku.count = 0
                    sudoku_resolver(sudoku)
            y += 1
        y = 0
        x += 1


sudoku_resolver(sudo)

print("AFTER RESOLVE")
for row in sudo.sudokuMatrice:
    print(row)
