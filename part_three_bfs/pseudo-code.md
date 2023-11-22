FONCTION `se déplace à` (`Coordonées`)
    `Coordonées` DE `Joueur` EST `Coordonées`

FONCTION `change de direction`
    QUEL EST `Direction` DE `Joueur` ?
        - `Sud`
            `Direction` DE `Joueur` EST `Est`
        - `Est`
            `Direction` DE `Joueur` EST `Nord`
        - `Nord`
            `Direction` DE `Joueur` EST `Ouest`
        - `Ouest`
            `Direction` DE `Joueur` EST `Sud`

FONCTION `regarde case en face`
    POUR CHAQUE `Case` DANS `Case adjacentes` DE `Joueur`
        SI `Direction` DE `Case` EST `Direction` DE `Joueur`
            RETOURNE `Case`

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
        SI `Case` N'EST PAS `Mur` ET `Coordonées` DE `Case` N'EST PAS DANS `Case visitées` DE `Joueur`
            AJOUT DE `Coordonées` DE `Case` DANS `Chemin` DE `Joueur`
    `Joueur` **se déplace à** PREMIÈRE `Coordonées` DANS `Chemin` DE `Joueur`
    RETIRE PREMIÈRE `Coordonées` DANS `Chemin` DE `Joueur`