# -*- coding: utf-8 -*-
class TennisGame3:
    def __init__(self, player1Name, player2Name):
        # TODO nommage de variable peu explicite, non conventionnel avec le langage également -> Trouver un meilleur nom
        self.p1N = player1Name
        self.p2N = player2Name
        # TODO appeler p1 player_1_score par exemple
        self.p1 = 0
        self.p2 = 0
    # TODO Nom de paramètre peu explicite -> transformer n en name
    def won_point(self, n):
        if n == "player1":
            self.p1 += 1
        else:
            self.p2 += 1
    # TODO Renommer la fonction afin de comprendre son usage ex : return_game_score
    def score(self):
        # TODO Créer des variables contenant les expressions booléennes
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            # TODO p et s ? Variables non explicites
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            print('test')
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1-self.p2)*(self.p1-self.p2) == 1) else "Win for " + s
