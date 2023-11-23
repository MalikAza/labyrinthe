FONCTION `se déplace à` (`Coordonées`)
    `Coordonées` DE `Joueur` EST `Coordonées`

// Tri des `Cases adjacentes`
    1- Sud
    2- Est
    3- Ouest
    4- Nord

`Direction` DE `Joueur` EST `Sud`
`Chemin` DE `Joueur` EST `Vide`
`Cases visitées` DE `Joueur` EST `Vide`
TANT QUE `Coordonées` de `Joueur` N'EST PAS `Coordonées` DE `Case de fin`
    SI `Coordonées` DE `Joueur` N'EST PAS DANS `Case visitées` DE `Joueur`
        AJOUT DE `Coordonées` DE `Joueur` DANS `Case visitées` DE `Joueur`
    POUR CHAQUE `Case` DANS `Case adjacentes` (trier) DE `Joueur`
        SI `Case` N'EST PAS `Mur` ET `Coordonnées` DE `Case` N'EST PAS DANS `Case visitées` DE `Joueur` ET `Coordonnées` DE `Case` N'EST PAS DANS `Chemin` DE `Joueur`
            AJOUT DE `Coordonnées` DE `Case` DANS `Chemin` DE `Joueur`
        SI `Case` EST `Case de fin`
            DERNIÈRES `Coordonnées` DANS `Chemin` DE `Joueur` EST `Coordonnées` DE `Case`
            FIN POUR CHAQUE 
    `Joueur` **se déplace à** PREMIÈRE `Coordonées` DANS `Chemin` DE `Joueur`
    RETIRE PREMIÈRE `Coordonées` DANS `Chemin` DE `Joueur`