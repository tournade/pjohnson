from joueur import Joueur
from combinaison import Combinaison
from random import shuffle

#changement a enleve

class Partie:
    """Représente une partie du jeu de Poker d'As

    Attributes:
        joueurs (list): La liste des joueurs.
    """


    def __init__(self, joueurs): # **** a completer ****
        """Initialise une partie avec la liste de joueurs

        Args:
            joueurs (list): La liste des joueurs.
        """


    def jouer_partie(self): # **** a completer ****
        """ Joue une partie entre tous les joueurs et détermine le gagnant.
        Le compteur du nombre de partie est incrémenté pour chacun des joueurs.
        Le compteur de victoires est incrémenté pour le joueur gagnant (si la partie n'est pas nulle).
        Le joueur gagnant est affiché à l'écran (ou un message indiquant que la partie est nulle, s'il y a lieu).
        """


    def _determiner_ordre(self): # **** a completer ****
        """Détermine l'ordre dans lequel les joueurs vont jouer.
        Return (list): La liste des index des joueurs indiquant l'ordre.

        Exemple:
            [2, 1, 0] indique que joueur 3 joue, suivi du joueur 2, puis du
            joueur 1.
        """




#***************************
# vous n etes pas obligés de garder ces tests - ils sont là pour vous aider a comprendre les methodes
# vous pouvez les modifier a votre guise
#***************************

if __name__ == "__main__":
    joueurs = [Joueur("a"), Joueur("b"), Joueur("c")]

    partie = Partie(joueurs)

    # Teste que tous les joueurs vont jouer une et une seule fois
    ordre = partie._determiner_ordre()
    assert len(ordre) == 3
    assert 0 in ordre
    assert 1 in ordre
    assert 2 in ordre
