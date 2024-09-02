from upemtk import *
from doctest import testmod

# Initialisation du jeu 
nbr_case = 8  # nbr de case sur une ligne ou une colonne
taille_case = 120  # en pixels
largeur_plateau = nbr_case * taille_case  # largeur de la fenêtre
hauteur_plateau = nbr_case * taille_case  # hauteur de la fenêtre
background_color = 'grey'
menu = True
somme_blanc = None
somme_noir = None
# pour plateau
plateau = [[0 for x in range(nbr_case)] for y in range(nbr_case)]  # creation d'une liste de liste avec que des 0
# pions disposés aux centres en début de partie
index = int(nbr_case / 2)
plateau[index - 1][index - 1] = -1
plateau[index][index - 1] = 1
plateau[index - 1][index] = 1
plateau[index][index] = -1
# pour plateau2
plateau2 = []


# FONCTIONS
def quadrillage():
    """
    Fonction qui dessine un quadrillage et met une couleur de fond
    """
    rectangle(0, 0, largeur_plateau, hauteur_plateau, couleur=background_color, remplissage=background_color,
              epaisseur=1)

    for i in range(nbr_case + 1):
        ax = i * taille_case
        ligne(ax, 0, ax, hauteur_plateau, couleur='black', epaisseur=1)

        ay = i * taille_case
        ligne(0, ay, largeur_plateau, ay, couleur='black', epaisseur=1)


def affiche_pion():
    """
    Fonction qui affiche les pions selon sa représentation dans la liste de listes plateau
    """
    for i in range(nbr_case):
        for c in range(nbr_case):

            if plateau[i][c] != 0:
                if plateau[i][c] == -1:
                    color = 'white'
                else:
                    color = 'black'

                x = c * taille_case + taille_case / 2
                y = i * taille_case + taille_case / 2
                rayon = taille_case / 3
                cercle(x, y, rayon, couleur=color, remplissage=color, epaisseur=1)


def copy_list():
    """
    Fonction pour copier plateau dans plateau2
    """
    global plateau2
    for i in range(nbr_case):
        for c in range(nbr_case):
            val = plateau[i][c]
            plateau2[i][c] = val


def remplir_case(q, c, color__code):
    """
    Fonction qui affiche des rectangles colorés (correspondant aux cases jouables)
    
    Paramètres:
         q : indice de la ligne où se situe la case (int)
         c : indice de la colonne où se situe la case (int)
         color_code : entier représentant le joueur actuel (1: joueur avec les pions noirs, -1:
                      joueur avec les pions blancs)
    """
    if color__code == -1:
        color = 'white'
    else:
        color = 'black'

    x1 = c * taille_case
    x2 = (c + 1) * taille_case
    y1 = q * taille_case
    y2 = (q + 1) * taille_case

    rectangle(x1, y1, x2, y2, couleur=color, remplissage=color, epaisseur=1)


def verif_souris(x, y, q, c, debut_l, debut_c, fin_l, fin_c, color__code):
    """
    Fonction vérifiant si l'on clique sur la case 
    et actualise la variable plateau (pions à retourner)
    
    PARAMETRES:
        x : abcisse du point cliqué (int)
        y : ordonnée du point cliqué (int)
        q : indice de la ligne où se situe la case (int)
        c : indice de la colonne où se situe la case (int)
        debut_l : indice de la ligne où se situe le premier pion qui doit être de la couleur du joueur
                  (pion le plus à gauche) (int)
        debut_c : indice de la colonne où se situe le premier pion qui doit être de la couleur du joueur
                  (pion le plus haut) (int)
        fin_l : indice de la ligne où se situe le dernier pion qui doit être de la couleur du joueur
                (pion le plus à droite) (int)
        fin_c : indice de la colonne où se situe le dernier pion qui doit être de la couleur du joueur
                (pion le plus bas) (int)
        color_code : entier représentant le joueur actuel (1: joueur avec les pions noirs, -1:
                     joueur avec les pions blancs)
    
    >>> verif_souris(533, 317, 2, 4, 2, 4, 4, 4, -1)
    True
    >>> verif_souris(1, 1, 2, 4, 2, 4, 4, 4, -1)
    False
    """
    x1 = c * taille_case
    x2 = (c + 1) * taille_case
    y1 = q * taille_case
    y2 = (q + 1) * taille_case
    action_ = False

    if x1 <= x <= x2 and y1 <= y <= y2:
        action_ = True
        for index_l in range(debut_l, fin_l + 1):
            for index_c in range(debut_c, fin_c + 1):
                plateau[index_l][index_c] = color__code

    return action_


def verification(color__code, coord_souris):
    """
    Vérifie que le joueur peut placer son pion à cette case
    (doit être sur la même ligne ou la même colonne qu’au moins un autre pion de sa couleur 
    et qu'entre ces deux pions, il n’y ait que des pions de l’autre couleur)
    - 1ere fois utilisée: appelle la fonction remplir_case
      et return True (quand on trouve des cases jouables) 
      utilisable quand les coordonnées de la souris ne sont pas utilisées (donc initialisation : x == -1)
    ou
    - 2eme fois utilisée: appelle la fonction verif_souris
    
    Paramètres:
        code_color : entier représentant le joueur actuel 
                    (1: joueur avec les pions noirs
                    -1: joueur avec les pions blancs)
        coord_souris : deux entiers séparés par une virgule représentant les coordonnées du point cliqué
                    (x, y)
    """
    global plateau
    global plateau2

    code_retour = False
    x, y = coord_souris
    code_color_opp = -color__code
    copy_list()

    # horizontal
    for L in range(nbr_case):
        pos_debut = -1
        pos_fin = -1

        for c in range(nbr_case):  # verifies horizontalement par exemple [-1, 1,..., 1,0]
            if plateau[L][c] == color__code:
                pos_debut = c
                pos_fin = -1
            elif plateau[L][c] == code_color_opp:
                pos_fin = c
            elif plateau[L][c] == 0:
                if pos_debut != -1 and pos_fin != -1:
                    if x == -1:
                        remplir_case(L, c, color__code)
                        code_retour = True
                    else:
                        tmp_retour = verif_souris(x, y, L, c, L, pos_debut, L, c, color__code)
                        if tmp_retour:
                            code_retour = True
                    break

        pos_debut = -1
        pos_fin = -1
        for c in range(nbr_case):  # verifies horizontalement par exemple [0, 1,..., 1,-1]
            if plateau[L][c] == 0:
                pos_debut = c
                pos_fin = -1
            elif plateau[L][c] == code_color_opp:
                pos_fin = c
            elif plateau[L][c] == color_code:
                if pos_debut != -1 and pos_fin != -1:
                    if x == -1:
                        remplir_case(L, pos_debut, color_code)
                        code_retour = True
                    else:
                        tmp_retour = verif_souris(x, y, L, pos_debut, L, pos_debut, L, pos_fin, color__code)
                        if tmp_retour:
                            code_retour = True
                    break

    # vertical
    for c in range(nbr_case):  # verifies verticalement par exemple [-1, 1,..., 1,0]
        pos_debut = -1
        pos_fin = -1
        for L in range(nbr_case):
            if plateau2[L][c] == color_code:
                pos_debut = L
                pos_fin = -1
            elif plateau2[L][c] == code_color_opp:
                pos_fin = L
            elif plateau2[L][c] == 0:
                if pos_debut != -1 and pos_fin != -1:
                    if x == -1:
                        remplir_case(L, c, color_code)
                        code_retour = True
                    else:
                        tmp_retour = verif_souris(x, y, L, c, pos_debut, c, L, c, color_code)
                        if tmp_retour:
                            code_retour = True
                    break

        pos_debut = -1
        pos_fin = -1
        for L in range(nbr_case):  # verifies verticalement par exemple [0, 1,..., 1,-1]
            if plateau2[L][c] == 0:
                pos_debut = L
                pos_fin = -1
            elif plateau2[L][c] == code_color_opp:
                pos_fin = L
            elif plateau2[L][c] == color_code:
                if pos_debut != -1 and pos_fin != -1:
                    if x == -1:
                        remplir_case(pos_debut, c, color_code)
                        code_retour = True
                    else:
                        tmp_retour = verif_souris(x, y, pos_debut, c, pos_debut, c, pos_fin, c, color_code)
                        if tmp_retour:
                            code_retour = True
                    break

    return code_retour


def comptage_pions(plateau_jeu):
    """
    Fonction comptant le nombre de pion de chaque joueur
    >>> comptage_pions([[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 1, 0, 0, 0], [0, 0, 0, 1, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])
    (2, 2)
    """
    somme__blanc = 0
    somme__noir = 0
    for i in range(nbr_case):
        for c in range(nbr_case):
            pion = plateau_jeu[i][c]

            if pion == -1:
                somme__blanc += 1
            elif pion == 1:
                somme__noir += 1

    return somme__blanc, somme__noir


print(testmod())

# PROGRAMME PRINCIPAL
while menu:
    # menu initialisation
    cree_fenetre(largeur_plateau, hauteur_plateau)

    # bouton jouer
    rectangle(taille_case * 2, taille_case * 2, largeur_plateau - (taille_case * 2), taille_case * 3, couleur='white',
              remplissage='black', epaisseur=1)
    texte(taille_case * 2 + taille_case * 4 / 3, taille_case * 2 + taille_case * 1 / 3, "Jouer", couleur='white')

    # bouton quitter
    rectangle(taille_case * 2, taille_case * 4, largeur_plateau - (taille_case * 2), taille_case * 5, couleur='white',
              remplissage='black', epaisseur=1)
    texte(taille_case * 2 + taille_case * 5 / 4, taille_case * 4 + taille_case * 1 / 3, "Quitter", couleur='white')

    while True:
        clic = attend_clic_gauche()

        # si clique sur bouton jouer
        if (taille_case * 2) <= clic[0] <= (
                largeur_plateau - (taille_case * 2)) and (taille_case * 2) <= clic[1] <= (taille_case * 3):
            ferme_fenetre()
            break
        # si clique sur bouton quitter
        elif (taille_case * 2) <= clic[0] <= (
                largeur_plateau - (taille_case * 2)) and (taille_case * 4) <= clic[1] <= (taille_case * 5):
            menu = False
            ferme_fenetre()
            break

    # quitter le programme
    if not menu:
        break

    # AFFICHAGE
    cree_fenetre(largeur_plateau, hauteur_plateau)
    nb_joueur = 2
    color_code = 1  # joueur, 1: joueur avec les pions noirs et -1: joueur avec les pions blancs

    # initialisation pour plateau
    plateau = [[0 for x in range(nbr_case)] for y in range(nbr_case)]  # creation d'une liste de liste avec que des 0
    # pions disposés aux centres en début de partie
    index = int(nbr_case / 2)
    plateau[index - 1][index - 1] = -1
    plateau[index][index - 1] = 1
    plateau[index - 1][index] = 1
    plateau[index][index] = -1
    # initialisation pour plateau2
    plateau2 = [[0 for x in range(nbr_case)] for y in range(nbr_case)]  # creation d'une liste de liste avec que des 0

    while True:
        color_code = (-1) * color_code  # pour passer d'un joueur à l'autre
        quadrillage()
        affiche_pion()

        position_souris = -1, -1  # initialisation au début de chaque tour
        situation_jouable = verification(color_code, position_souris)  # traçage des cases jouables

        if not situation_jouable:  # si un joueur est obligé de passer son tour
            nb_joueur -= 1

            if nb_joueur == 0:
                somme_blanc, somme_noir = comptage_pions(plateau)
                break
            elif nb_joueur == 1:
                if color_code == -1:
                    texte(10, taille_case, "le joueur blanc passe son tour", couleur='red', taille=15)
                elif color_code == 1:
                    texte(10, taille_case, "le joueur noir passe son tour", couleur='red', taille=15)
                attend_clic_gauche()
                continue
            else:
                continue
        else:
            if nb_joueur != 2:
                nb_joueur = 2

        action = False
        while not action:  # tant qu'on ne clique pas sur une des cases jouables
            position_souris = attend_clic_gauche()
            action = verification(color_code,
                                  position_souris)  # vérification position cliqué par rapport aux cases jouables

    # Fin de jeu
    efface_tout()
    texte(taille_case * 2, taille_case * 2, "GAME OVER", couleur='black')
    texte(taille_case * 5 / 2, taille_case * 3, f"Score\nblanc:{somme_blanc}\nnoir:{somme_noir}", couleur='black')
    if somme_blanc == somme_noir:
        texte(taille_case * 2, taille_case * 4, "Égalité", couleur='black')
    elif somme_blanc > somme_noir:
        texte(taille_case * 2, taille_case * 5, "Blanc a gagné !", couleur='black')
    else:
        texte(taille_case * 2, taille_case * 5, "Noir a gagné !", couleur='black')

    attend_clic_gauche()
    ferme_fenetre()
