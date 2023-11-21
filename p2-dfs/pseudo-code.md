FUNCTION **Case Adjacentes** (x, y, xMax, yMax)
    `Case Nord` = y-1 < 0 ? `Mur` : y-1, x
    `Case Sud` = y+1 > yMax ? `Mur` : y+1, x
    `Case Est` = x+1 > xMax ? `Mur` : y, x+1
    `Case West` = x-1 < 0 ? `Mur` : y, x-1
    `Cases` = `Case Nord`, `Case Sud`, `Case Est`, `Case West`
    RETOURNE `Cases`

FUNCTION **Prochaine Direction** (direction_actuel)
    SI `direction_actuel` EST `Sud`
        RETOURNE `Est`
    SI `direction_actuel` EST `Est`
        RETOURNE `Nord`
    SI `direction_actuel` EST `Nord`
        RETOURNE `West`
    SI `direction_actuel` EST `West`
        RETOURNE `Sud`

`Direction du Joueur` EST `Sud`
`Case visités` EST `Vide`
`Changement de direction` EST `0`
`Essais` EST `0`
TANT QUE `Case du Joueur` N'EST PAS `Goal`
    `Joueur` **REGARDE** `Case directement adjacentes à Joueur`
    POUR CHAQUE `Case adjacentes`
        SI `Case adjacente` EST `Goal`
            `Joueur` **SE DEPLACE À** `Case adjacente`
            FIN
    SI `Case adjacente` DE `Direction du Joueur` N'EST PAS `Mur` ET N'EST PAS DANS `Case visités`
        `Case visités` += `Case actuelle du joueur`
        `Essais` EST `0`
        `Joueur` **SE DEPLACE À** `Case adjacente` DE `Direction du Joueur`
    SINON
        SI `Essais` >= 3
            `Nouveau chemin` EST `Faux`
            TANT QUE `Nouveau chemin` N'EST PAS `Vrai`
                `Joueur` **SE DEPLACE À** DERNIER `Case visités`
                `Enlever` DERNIER `Case visités`
                `Joueur` **REGARDE** `Case directement adjacentes à Joueur`
                POUR CHAQUE `Case adjacentes`
                    SI `case adjacente` N'EST PAS `Mur` ET N'EST PAS DANS `Case visités`
                        `Direction du joueur` EST `direction` DE `case adjacente`
                        `Nouveau chemin` EST `Vrai`
        SINON
            `Direction du Joueur` EST **Prochaine Direction**
            `Essais` += 1