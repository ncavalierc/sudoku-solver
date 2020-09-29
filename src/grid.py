# -*-coding: utf8-*-
import sys


class SudokuGrid:
    """Cette classe représente une grille de Sudoku.
    Toutes ces méthodes sont à compléter en vous basant sur la documentation fournie en docstring.
    """

    def __init__(self, initial_values_str=""):
        """À COMPLÉTER!
        Ce constructeur initialise une nouvelle instance de la classe SudokuGrid.
        Il doit effectuer la conversation de chaque caractère de la chaîne en nombre entier,
        et lever une exception (ValueError) si elle ne peut pas être interprétée comme une grille de Sudoku.
        :param initial_values_str: Une chaîne de caractères contenant **exactement 81 chiffres allant de 0 à 9**,
            où ``0`` indique une case vide
        :type initial_values_str: str
        """
        self.grid_values = []
        try:
            for i in initial_values_str:
                self.grid_values.append(int(i))
        except Exception as e:
            print("{}: {}".format(type(e).__name__, e))


    @staticmethod
    def from_file(filename, line):
        """À COMPLÉTER!
        Cette méthode de classe (ou méthode statique) crée une nouvelle instance de grille de Sudoku
        à partir d'une ligne contenue dans un fichier.

        :param filename: Chemin d'accès vers le fichier à lire
        :param line: Numéro de la ligne à lire
        :type filename: str
        :type line: int
        :return: La grille de Sudoku correspondant à la ligne donnée dans le fichier donné
        :rtype: SudokuGrid
        """
        grid = SudokuGrid()
        file = open(filename, "r")
        for i in file:
            if i == line-1:
                grid = SudokuGrid(file.readline(line,line))
        return grid
        file.close()

    @staticmethod
    def from_stdin():
        """À COMPLÉTER!
        Cette méthode de classe crée une nouvelle instance de grille de Sudoku
        à partir d'une ligne lu depuis l'entrée standard (saisie utilisateur).
        *Variante avancée: Permettez aussi de «piper» une ligne décrivant un Sudoku.*
        :return: La grille de Sudoku correspondant à la ligne donnée par l'utilisateur
        :rtype: SudokuGrid
        """
        #line = sys.stdin.read()
        #if line == "":
        line = input("Saisissez votre ligne de sudoku -> ")
        return SudokuGrid(line)


    def affiche(self):
        j, k, l = 0, 0, 0
        print()
        for i in self.grid_values:
            if k == 0 and j == 0:
                print("||", end="")
            print(" {} ".format(i), end="|")
            j += 1
            if j == 3:
                print("|", end="")
                k += 1
                j = 0
            if k == 3:
                l += 1
                if l == 3:
                    print()
                    print("=========================================")
                    l = 0
                else:
                    print()
                    print("-----------------------------------------")
                k = 0


    def __str__(self):
        """À COMPLÉTER!
        Cette méthode convertit une grille de Sudoku vers un format texte pour être affichée.
        :return: Une chaîne de caractère (sur plusieurs lignes...) représentant la grille
        :rtype: str
        """
        lines = ""
        j, k = 0, 0
        for i in self.grid_values:
            lines = lines + str(i)
            j += 1
            if j == 9:
                lines += "\n"
                j = 0
        self.affiche()
        return lines



    def get_row(self, i):
        """À COMPLÉTER!
        Cette méthode extrait une ligne donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param i: Numéro de la ligne à extraire, entre 0 et 8
        :type i: int
        :return: La liste des valeurs présentes à la ligne donnée
        :rtype: list of int
        """
        start_index = 9 * (i)
        end_index = 9 * (i+1)
        line = self.grid_values[start_index:end_index]
        return line

    def get_col(self, j):
        """À COMPLÉTER!
        Cette méthode extrait une colonne donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param j: Numéro de la colonne à extraire, entre 0 et 8
        :type j: int
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of int
        """
        col = []
        for i in range(j, 81, 9):
            col.append(self.grid_values[i])
        return col

    def get_region(self, reg_row, reg_col):
        """À COMPLÉTER!
        Cette méthode extrait les valeurs présentes dans une région donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param reg_row: Position verticale de la région à extraire, **entre 0 et 2**
        :param reg_col: Position horizontale de la région à extraire, **entre 0 et 2**
        :type reg_row: int
        :type reg_col: int
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of int
        """
        start_row, end_row = 3*reg_row, 3*reg_row + 3
        start_col, end_col = 3*reg_col, 3*reg_col + 3
        print(start_row, start_col)
        region = []

        for j in range(start_row, end_row):
            for i in range(start_col, end_col):
                val = j*9 + i
                region.append(self.grid_values[val])
        return region

    def get_empty_pos(self):
        """À COMPLÉTER!
        Cette méthode renvoit les positions des cases vides dans la grille de Sudoku,
        sous la forme de tuples ``(i,j)`` où ``i`` est le numéro de ligne et ``j`` le numéro de colonne.
        *Variante avancée: Renvoyez un générateur sur les tuples de positions ``(i,j)`` au lieu d'une liste*
        :return: La liste des positions des cases vides dans la grille
        :rtype: list of tuple of int
        """
        empty_pos = []
        for i in range(81):
            if self.grid_values[i] == 0:
                tup = (, )
                empty_pos.append(tup)
        print(empty_pos)
        return empty_pos

    def write(self, i, j, v):
        """À COMPLÉTER!
        Cette méthode écrit la valeur ``v`` dans la case ``(i,j)`` de la grille de Sudoku.
        *Variante avancée: Levez une exception si ``i``, ``j`` ou ``v``
        ne sont pas dans les bonnes plages de valeurs*
        *Variante avancée: Ajoutez un argument booléen optionnel ``force``
        qui empêche d'écrire sur une case non vide*
        :param i: Numéro de ligne de la case à mettre à jour, entre 0 et 8
        :param j: Numéro de colonne de la case à mettre à jour, entre 0 et 8
        :param v: Valeur à écrire dans la case ``(i,j)``, entre 1 et 9
        """
        raise NotImplementedError()

    def copy(self):
        """À COMPLÉTER!
        Cette méthode renvoie une nouvelle instance de la classe SudokuGrid,
        qui doit être une copie **indépendante** de la grille de Sudoku.
        *Variante avancée: vous pouvez utiliser ``self.__new__(self.__class__)``
        pour court-circuiter l'appel à ``__init__`` et manuellement initialiser les attributs de la copie.*
        :return: Une copie de la grille courrante
        :rtype: SudokuGrid
        """
        raise NotImplementedError()
