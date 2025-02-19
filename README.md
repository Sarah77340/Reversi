# Reversi – Jeu à Deux Joueurs  

## Objectifs  
Ce projet consiste à programmer **Reversi** en Python avec les fonctionnalités de base suivantes :  

- Affichage d'un **plateau 8x8** avec les **4 pions initiaux** placés au centre.  
- Possibilité pour les **deux joueurs** de jouer chacun leur tour en cliquant sur une case jouable.  
- **Retourner** les pions adverses encadrés après chaque coup.  
- **Détection de la fin de partie** :  
  - Lorsque toutes les cases sont remplies.  
  - Lorsqu’aucun joueur ne peut plus jouer.  
- Affichage du **vainqueur** en fonction du nombre de pions.  

## Améliorations  
- Un **menu principal** a été ajouté pour faciliter l'accès au jeu.  
- Ajout d’un bouton **"Jouer"** pour démarrer la partie et d’un bouton **"Quitter"** pour fermer le jeu.  

## Documentation utilisateur  

Le jeu **Reversi** suit ces règles :  

1. **Lancer le jeu** : Cliquez sur le bouton `"Jouer"` dans le menu principal.  
2. **Configuration initiale** : Le plateau **8x8** s'affiche avec **4 pions** placés au centre.  
3. **Déroulement de la partie** :  
   - Le joueur avec les **pions blancs** commence.  
   - Les joueurs placent leurs pions en cliquant sur une **case valide**.  
   - Les **pions adverses encadrés** sont retournés.  
   - Si un joueur ne peut pas jouer, il passe son tour.  
4. **Fin de partie** :  
   - Lorsque toutes les cases sont remplies.  
   - Lorsque **aucun joueur ne peut jouer**.  
   - Le joueur avec le **plus de pions de sa couleur** gagne.  
5. **Retour au menu** : À la fin de la partie, un clic permet de revenir au menu principal.  

## Documentation technique  

### Bibliothèques utilisées  

- `doctest` → Pour tester les fonctions.  
- `upemtk` → Pour gérer l'affichage graphique et les interactions avec la souris.  

### Fonctions principales  

| Fonction             | Rôle |
|----------------------|---------------------------------------------------|
| `quadrillage()`      | Dessine le **plateau de jeu** avec une grille 8x8. |
| `affiche_pion()`     | Affiche les pions sur le plateau en fonction d’une **liste de listes**. |
| `copy_list()`        | Crée une **copie du plateau** pour éviter les modifications directes. |
| `remplir_case()`     | Indique **les cases jouables** en les colorant. |
| `verif_souris()`     | Vérifie si un clic a été effectué sur une **case jouable**. |
| `verification()`     | Détermine les **cases valides** et gère le **retournement des pions**. |
| `comptage_pions()`   | Compte le **nombre de pions** de chaque joueur. |

### Fonctionnement général  

1. **Menu principal** : Création d’une fenêtre avec **"Jouer"** et **"Quitter"**.  
2. **Lancement de la partie** :  
   - Création du plateau **(8x8)**.  
   - Initialisation du **tableau des pions**.  
   - Alternance entre les joueurs avec `code_color` (1 pour blanc, -1 pour noir).  
3. **Gestion du jeu** :  
   - Affichage des **cases jouables**.  
   - Vérification du **coup joué** et retournement des pions si nécessaire.  
4. **Fin du jeu** : Affichage du **score final** et attente du clic pour fermer la fenêtre.  

## Auteurs
- **Mohamed Alla**  
- **Nguyen Sarah**  
