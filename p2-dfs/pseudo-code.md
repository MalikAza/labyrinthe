FONCTION `se déplace à` (`Coordonées`)
    `Coordonées` DE `Joueur` EST `Coordonées`

FONCTION `reviens sur son chemin`
    `Coordonées` EST `Dernière Coordonées` DE `Chemin` DE `Joueur`
    ENLEVER `Dernière Coordonées` DE `Chemin` DE `Joueur`
    `Joueur` **se déplace à** `Coordonées`

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

`Direction` DE `Jouer` EST `Sud`
`Cases visitées` DE `Joueur` EST VIDE
`Chemin` DE `Joueur` EST VIDE
`Essais` EST `0`
TANT QUE `Coordonées du joueur` N'EST PAS `Coordonnées de case de fin`
    POUR CHAQUE `Case` DANS `Cases adjacentes à joueur`
        SI `Case` EST `Fin`
            `Joueur` **se déplace à** `Coordonées` DE `Case`
            FIN
        SI `Direction` DE `Case` EST `Direction` DE `Joueur`
            `Case en face de joueur` EST `Case`
    SI `Case en face de joueur` EST `Mur` ET N'EST PAS DANS `Cases visitées` DE `Joueur`
        AJOUT DE `Coordonées` DE `Joueur` À `Cases visitées` DE `Joueur`
        AJOUT DE `Coordonées` DE `Joueur` À `Chemin` DE `Joueur`
        `Essais` EST `0`
        `Joueur` **se déplace à** `Coordonées` DE `Case en face de joueur`
    SINON SI `Essais` N'EST PAS `3`
        `Joueur` **change de direction**
        `Essais` += 1
    SINON
        SI `Coordonées` DE `Joueur` N'EST PAS DANS `Cases visitées` DE `Joueur`
            AJOUT DE `Coordonées` DE `Joueur` À `Cases visitées` DE `Joueur`
        `Joueur` **reviens sur son chemin**
        `Essais` EST `0`