class TennisGame5:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1
        else:
            raise ValueError("Invalid player name.")
    
    def get_score(self):
        score_map = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        
        if self.player1_score >= 4 or self.player2_score >= 4:
            if abs(self.player1_score - self.player2_score) >= 2:
                return f"Win for {self.player1_name if self.player1_score > self.player2_score else self.player2_name}"
            elif self.player1_score == self.player2_score:
                return "Deuce"
            else:
                return f"Advantage {self.player1_name if self.player1_score > self.player2_score else self.player2_name}"
        
        if self.player1_score == self.player2_score:
            return f"{score_map[self.player1_score]}-All" if self.player1_score < 3 else "Deuce"
        
        return f"{score_map[self.player1_score]}-{score_map[self.player2_score]}"

def play_game(TennisGameClass, p1_points, p2_points, p1_name, p2_name):
    game = TennisGameClass(p1_name, p2_name)
    for _ in range(p1_points):
        game.won_point(p1_name)
    for _ in range(p2_points):
        game.won_point(p2_name)
    return game

test_cases = [
    (0, 0, "Love-All", "player1", "player2"),
    (1, 0, "Fifteen-Love", "player1", "player2"),
    (2, 1, "Thirty-Fifteen", "player1", "player2"),
    (3, 2, "Forty-Thirty", "player1", "player2"),
    (4, 3, "Advantage player1", "player1", "player2"),
    (3, 3, "Deuce", "player1", "player2"),
    (4, 4, "Deuce", "player1", "player2"),
    (4, 0, "Win for player1", "player1", "player2"),
    (0, 4, "Win for player2", "player1", "player2"),
]