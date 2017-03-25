from joueur import Joueur
from combinaison import Combinaison
from random import shuffle


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
        self.joueurs = joueurs
        self.nombre_de_lancer = 0

    def jouer_partie(self): # **** a completer ****
        """ Joue une partie entre tous les joueurs et détermine le gagnant.
        Le compteur du nombre de partie est incrémenté pour chacun des joueurs.
        Le compteur de victoires est incrémenté pour le joueur gagnant (si la partie n'est pas nulle).
        Le joueur gagnant est affiché à l'écran (ou un message indiquant que la partie est nulle, s'il y a lieu).
        """
        print ("L'ordre est tiré au hasard")
        ordre = self._determiner_ordre()
        player = 1
        resultat_list = []
        print()
        for i in ordre:
            print("Le joueur", player, "est", self.joueurs[i])
            player += 1
        print()
        for i in ordre:
            print("C'est au tour de", self.joueurs[i])
            combinaison_final = self.joueurs[i].jouer_tour(self.nombre_de_lancer)
            if self.nombre_de_lancer == 0:
                self.nombre_de_lancer = self.joueurs[i].combinaison_des.nb_lancers
            resultat_list.append((self.joueurs[i].nom,self.joueurs[i].resultat))
            print()
        gagnant = Combinaison.determiner_meilleur_combinaison(resultat_list)
        for player_gagnant in self.joueurs:
            player_gagnant.nb_parties_jouees += 1
            if gagnant[0] == player_gagnant.nom:
                player_gagnant.nb_victoires += 1

        if gagnant[1] == None:
            print("la parti est null")
        else:
            print("le gagnant est", gagnant[0], "avec un", gagnant[1])

        print()

    def _determiner_ordre(self): # **** a completer ****
        """Détermine l'ordre dans lequel les joueurs vont jouer.
        Return (list): La liste des index des joueurs indiquant l'ordre.

        Exemple:
            [2, 1, 0] indique que joueur 3 joue, suivi du joueur 2, puis du
            joueur 1.
        """
        random_list = []
        for i in range(0,len(self.joueurs)):
            random_list.append(i)

        shuffle(random_list)
        return random_list

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
