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

    def __init__(self, des = None): # **** a completer ****
        """Initialise une combinaison"""


    def relancer_des(self, index_a_relancer): # **** a completer ****
        """Relance les dés spécifiés
        Args:
            index_a_relancer (list): Liste des index des dés à relancer.
        """


    def determiner_type_combinaison(self): # **** a completer ****
        """Détermine le type de la combinaison.

        Return (TypeCombinaison): Le type de la combinaison.
        """


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



    def _lancer_des(self, n): # **** a completer ****
        """Lance n dés.

        Args:
            n (int): Le nombre de dés à lancer.
        """


    def __str__(self): # **** a completer ****
        '''
        a vous de voir comment definir et utiliser
        :return: a definir selon vos besoins
        '''



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
    combinaison.relancer_des([])
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
            ([Carte.AS, Carte.AS, Carte.AS, Carte.AS, Carte.AS],
             TypeCombinaison.QUINTON),
             ([Carte.ROI, Carte.AS, Carte.VALET, Carte.DIX, Carte.NEUF],
              TypeCombinaison.SEQUENCE),
             ([Carte.VALET] * 4 + [Carte.AS], TypeCombinaison.QUINTON),
             ([Carte.VALET] * 3 + [Carte.AS, Carte.ROI], TypeCombinaison.CARRE),
             ([Carte.VALET] * 2 + [Carte.ROI, Carte.AS, Carte.ROI],
              TypeCombinaison.FULL),
             ([Carte.VALET] * 2 + [Carte.ROI, Carte.AS, Carte.DAME],
              TypeCombinaison.BRELAN),
             ([Carte.ROI, Carte.DAME, Carte.AS, Carte.DIX, Carte.NEUF],
              TypeCombinaison.SEQUENCE),
             # Combinaisons sans As
             ([Carte.VALET] * 5, TypeCombinaison.QUINTON),
             ([Carte.VALET] * 4 + [Carte.ROI], TypeCombinaison.CARRE),
             ([Carte.VALET] * 3 + [Carte.ROI] * 2, TypeCombinaison.FULL),
             ([Carte.VALET] * 3 + [Carte.ROI, Carte.DAME], TypeCombinaison.BRELAN),
             ([Carte.AS, Carte.ROI, Carte.DAME, Carte.VALET, Carte.DIX],
              TypeCombinaison.SEQUENCE),
             ([Carte.ROI, Carte.DAME, Carte.VALET, Carte.DIX, Carte.NEUF],
              TypeCombinaison.SEQUENCE),
             ([Carte.ROI, Carte.ROI, Carte.VALET, Carte.VALET, Carte.NEUF],
              TypeCombinaison.DEUX_PAIRES),
             ([Carte.ROI, Carte.ROI, Carte.DIX, Carte.VALET, Carte.NEUF],
              TypeCombinaison.UNE_PAIRE)
             ]

    for des, vrai_type in combinaisons:
        shuffle(des)
        combinaison.des = des
        type = combinaison.determiner_type_combinaison()
        assert type == vrai_type
