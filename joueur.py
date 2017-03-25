from combinaison import Combinaison


class Joueur:
    """Classe représentant un joueur.

    Attributes:
        nom (str): Le nom du joueur
        nb_victoires (int): Le nombre de parties remportées.
        nb_parties_jouees (int): Le nombre de parties jouées.
    """
    def __init__(self, nom): # **** a completer ****
        """
        Initialise un nouveau joueur avec son nom.

        Args:0
            nom (str): Le nom du joueur.
        """
        self.nom = nom
        self.nb_victoires = 0
        self.nb_parties_jouees = 0




    def jouer_tour(self, limite_lancers): # **** a completer ****
        """
        Joue le tour d'un joueur.
        Args:
            limite_lancers (int): Le nombre de lancers maximums.

        Returns (Combinaison): La combinaison obtenue

        """
        self.combinaison_des = Combinaison(des=5)
        print(self.combinaison_des)
        continuer = True
        while(limite_lancers != self.combinaison_des.nb_lancers and self.combinaison_des.nb_lancers != 3 and continuer ):
            selection = input("Quel(s) dé(s) voulez-vous rejouer (0 pour aucun), entrez la liste (ex. 1,5) : ")
            if selection == "0":
                continuer = False
            else:
                emplacement_de = selection.split(",")
                self.combinaison_des.relancer_des(emplacement_de)
                print(self.combinaison_des)
        self.resultat = self.combinaison_des.determiner_type_combinaison()
        print(self.nom,"a eu",self.resultat)
        return self.combinaison_des.des

    def __str__(self): # **** a completer ****
        """
        Converti le joueur en une chaîne de caractères le représentant (le nom du joueur).
        Returns (str): La chaîne de caractères représentant le joueur.

        """
        return self.nom
