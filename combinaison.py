from enums import Carte, TypeCombinaison
from random import choice, shuffle


class Combinaison:
    """Représente la combinaison d'un joueur

    Attributes:
        des (list): Liste des dés lancés.
        nb_lancers (int): Le nombre de lancers réalisés.
        types_cartes (list): Les différents types de cartes.
    """
    types_de = [
        Carte.AS, Carte.ROI, Carte.DAME, Carte.VALET, Carte.DIX, Carte.NEUF
    ]

    def __init__(self, des = 5): # **** a completer ****
        """Initialise une combinaison"""
        self.des = self._lancer_des(des)
        self.nb_lancers = 1


    def relancer_des(self, index_a_relancer): # **** a completer ****
        """Relance les dés spécifiés
        Args:
            index_a_relancer (list): Liste des index des dés à relancer.
        """
        compteur = 0
        if index_a_relancer[0] != '':
            new_de = self._lancer_des(len(index_a_relancer))
            self.nb_lancers += 1
            for x in index_a_relancer:
                self.des[int(x) - 1] = new_de[compteur]
                compteur += 1

    def determiner_type_combinaison(self): # **** a completer ****
        """Détermine le type de la combinaison.

        Return (TypeCombinaison): Le type de la combinaison.
        """
        self.des_combinaison = [0] * 6  # 6 car six valeurs sur le dé
        for i in range(len(self.des)):
            self.des_combinaison[self.des[i].value] += 1

        maximun = max(self.des_combinaison[1:])
        if self.des_combinaison[1:].count(1) != 4:
            for i in range(len(self.des_combinaison[1:])):
              if self.des_combinaison[1:][i] == maximun:
                  self.des_combinaison[i + 1] += self.des_combinaison[0]
                  self.des_combinaison[0] = 0

        if 5 in self.des_combinaison:
            return (TypeCombinaison.QUINTON)

        if 4 in self.des_combinaison:
            return (TypeCombinaison.CARRE)

        if 3 in self.des_combinaison and 2 in self.des_combinaison:
            return (TypeCombinaison.FULL)

        if 3 in self.des_combinaison and 2 not in self.des_combinaison:
            return (TypeCombinaison.BRELAN)

        if self.des_combinaison.count(1) == 5:
            return (TypeCombinaison.SEQUENCE)

        if self.des_combinaison.count(2) == 2:
            return (TypeCombinaison.DEUX_PAIRES)

        if self.des_combinaison.count(2) == 1 and 3 not in self.des_combinaison:
            return (TypeCombinaison.UNE_PAIRE)

        return (TypeCombinaison.AUTRE)  # tous les if sont donc False


    @staticmethod
    def determiner_meilleur_combinaison(combinaisons): # **** a completer ****
        """
        Méthode statique qui détermine la meilleure combinaison (et donc le meilleur joueur) parmi une liste.
        Args:
            combinaisons (list): Liste de combinaisons sous forme de liste de tuples (Joueur, Combinaison)

        Returns (tuple): Un tuple (Joueur, Combinaison) du meilleur joueur et de la meilleur combinaison ou (None, None)
                         en cas d'égalité. Il est à noter que le premier élément du tuple n'est pas nécessairement de
                         type Joueur. Ce peut être un object quelconque (Joueur, entier, string, etc.), selon
                         l'utilisation souhaitée.

        """

        resultat_gagnant =(None,None)
        max_resultat = 0
        for main in combinaisons:
            if main[1].value > max_resultat:
                max_resultat = main[1].value
                resultat_gagnant = main
            elif main[1].value == max_resultat:
                resultat_gagnant = (None, None)

        return resultat_gagnant

    def _lancer_des(self, n): # **** a completer ****
        """Lance n dés.

        Args:
            n (int): Le nombre de dés à lancer.
        """
        list_de = []
        for y in range(0, n):
            list_de.append(choice(self.types_de))
        return list_de

    def __str__(self): # **** a completer ****
        '''
        a vous de voir comment definir et utiliser
        :return: a definir selon vos besoins
        '''
        return "\nVoici votre combinaison:\nDés:     1  2  3  4  5\nValeur:  "+str(self.des[0]) + "  " + str(self.des[1]) + "  " + str(self.des[2]) + "  " + str(self.des[3]) + "  " + str(self.des[4]) + "\n"



#***************************
# vous n etes pas obligés de garder ces tests - ils sont là pour vous aider a comprendre les methodes
# vous pouvez les modifier a votre guise
#***************************

if __name__ == "__main__":
    combinaison = Combinaison()

    # Test de init
    assert len(combinaison.des) == 5
    assert combinaison.nb_lancers == 1

    # Test de relancer_des
    combinaison.relancer_des([''])
    assert combinaison.nb_lancers == 1
    anciens_des = list(combinaison.des)
    combinaison.relancer_des([3, 4])
    assert combinaison.nb_lancers == 2
    assert combinaison.des[0:2] == anciens_des[0:2]

    # Test de _lancer_des
    assert len(combinaison._lancer_des(5)) == 5
    assert len(combinaison._lancer_des(0)) == 0
    des = combinaison._lancer_des(5)
    for elem in des:
        assert isinstance(elem, Carte)

    # Test de str()
    combinaison.des = combinaison.types_de[0:5]
    assert "Dés:     1  2  3  4  5" in str(combinaison)
    assert "Valeur:  A  R  D  V  X" in str(combinaison)

    # Tests unitaires de determiner_type

    combinaisons = [
             # Combinaisons avec As
             ([Carte.AS, Carte.AS, Carte.AS, Carte.AS, Carte.AS], TypeCombinaison.QUINTON),
             ([Carte.ROI, Carte.AS, Carte.VALET, Carte.DIX, Carte.NEUF], TypeCombinaison.SEQUENCE),
             ([Carte.VALET] * 4 + [Carte.AS], TypeCombinaison.QUINTON),
             ([Carte.VALET] * 3 + [Carte.AS, Carte.ROI], TypeCombinaison.CARRE),
             ([Carte.VALET] * 2 + [Carte.ROI, Carte.AS, Carte.ROI], TypeCombinaison.FULL),
             ([Carte.VALET] * 2 + [Carte.ROI, Carte.AS, Carte.DAME], TypeCombinaison.BRELAN),
             ([Carte.ROI, Carte.DAME, Carte.AS, Carte.DIX, Carte.NEUF], TypeCombinaison.SEQUENCE),
             # Combinaisons sans As
             ([Carte.VALET] * 5, TypeCombinaison.QUINTON),
             ([Carte.VALET] * 4 + [Carte.ROI], TypeCombinaison.CARRE),
             ([Carte.VALET] * 3 + [Carte.ROI] * 2, TypeCombinaison.FULL),
             ([Carte.VALET] * 3 + [Carte.ROI, Carte.DAME], TypeCombinaison.BRELAN),
             ([Carte.AS, Carte.ROI, Carte.DAME, Carte.VALET, Carte.DIX], TypeCombinaison.SEQUENCE),
             ([Carte.ROI, Carte.DAME, Carte.VALET, Carte.DIX, Carte.NEUF], TypeCombinaison.SEQUENCE),
             ([Carte.ROI, Carte.ROI, Carte.VALET, Carte.VALET, Carte.NEUF], TypeCombinaison.DEUX_PAIRES),
             ([Carte.ROI, Carte.ROI, Carte.DIX, Carte.VALET, Carte.NEUF], TypeCombinaison.UNE_PAIRE)
             ]

    for des, vrai_type in combinaisons:
        shuffle(des)
        combinaison.des = des
        type = combinaison.determiner_type_combinaison()
        assert type == vrai_type
