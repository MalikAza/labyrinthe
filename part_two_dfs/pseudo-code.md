FONCTION `se déplace à` (`Coordonées`)
    `Coordonées` DE `Joueur` EST `Coordonées`

// Tri des `Cases adjacentes`
    1- Sud
    2- Est
    3- Ouest
    4- Nord

FONCTION `reviens sur son chemin`
    `Coordonées` EST `Dernière Coordonées` DE `Chemin` DE `Joueur`
    ENLEVER `Dernière Coordonées` DE `Chemin` DE `Joueur`
    `Joueur` **se déplace à** `Coordonées`

TANT QUE `Coordonnées` DE `Joueur` N'EST PAS `Coordonnées` DE `Case de fin`
    SI `Coordonnées` DE `Joueur` N'EST PAS DANS `Coordonnées visitées` DE `Joueur`
        AJOUT DE `Coordonnées` DE `Joueur` DANS `Coordonnées visitées` DE `Joueur`
    POUR CHAQUE `Case` DANS `Cases adjacentes` (trier) DE `Joueur`
        SI `Case` EST `Fin`
            `Joueur` **se déplace à** `Coordonées` DE `Case`
            FIN
    `Joueur s'est déplacé` EST `Faux`
    POUR CHAQUE `Case` DANS `Cases adjacentes` (trier) DE `Joueur`
        SI `Case` N'EST PAS `Mur` ET N'EST PAS DANS `Coordonnées visitées` DE `Joueur`
            AJOUT DE `Coordonées` DE `Joueur` À `Chemin` DE `Joueur`:
            `Joueur` **se déplace à** `Coordonnées` DE `Case`
            `Joueur s'est déplacé` EST `Vrai`
            FIN POUR CHAQUE
    SI `Joueur s'est déplacé` EST `Vrai`
        REVENIR AU DEBUT DE TANT QUE
    `Joueur` **reviens sur son chemin**