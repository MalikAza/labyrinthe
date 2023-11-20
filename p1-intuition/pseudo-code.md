FUNCTION **Case Adjacentes** (x, y, xMax, yMax)
    `Case Haute` = y-1 < 0 ? `Mur` : y-1, x
    `Case Basse` = y+1 > yMax ? `Mur` : y+1, x
    `Case Droite` = x+1 > xMax ? `Mur` : y, x+1
    `Case Gauche` = x-1 < 0 ? `Mur` : y, x-1
    `Cases` = `Case Haute`, `Case Basse`, `Case Droite`, `Case Gauche`
    RETOURNER `Cases`

FUNCTION **Prochaine Direction** (direction_actuel)
    SI `direction_actuel` EST `BAS`
        RETOURNE `Droite`
    SI `direction_actuel` EST `Droite`
        RETOURNE `Haut`
    SI `direction_actuel` EST `Haut`
        RETOURNE `Gauche`
    SI `direction_actuel` EST `Gauche`
        RETOURNE `Bas`

`Direction du Joueur` EST `BAS`
TANT QUE `Case du Joueur` N'EST PAS `Goal`
    `Joueur` **REGARDE** `Case directement adjacentes à Joueur`
    POUR CHAQUE `Case adjacentes`
        SI `Case Adjacente` EST `Goal`
            `Joueur` **SE DEPLACE À** `Case Adjacente`
            FIN
    `Déplacement Joueur` EST `Faux`
    TANT QUE `Déplacement Joueur` N'EST PAS `Vrai`
        SI `Case adjacentes` DE `Direction du Joueur` N'EST PAS `Mur`
            SI `Case adjacentes` DE `Direction du Joueur` N'EST PAS `Visité`
                `Joueur` **SE DEPLACE À** `Case adjacentes` DE `Direction du Joueur`
                `Case du Joueur` EST `Visité`
                `Déplacement Joueur` EST `Vrai`
            SINON
                POUR CHAQUE `Case adjacentes`
                    SI `Case adjacente` N'EST PAS `Mur` ET N'EST PAS `Visité`
                        `Direction du Joueur` EST `Direction` DE `Case adjacente`
                `Joueur` **SE DEPLACE À** `Case adjacentes` DE `Direction du Joueur`
                `Déplacement Joueur` EST `Vrai`
        SINON
            `Direction du Joueur` EST **PROCHAINE** `Directions`