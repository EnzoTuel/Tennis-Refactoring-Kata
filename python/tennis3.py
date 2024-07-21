class TennisGame3:
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
        score_map = ["Love", "Fifteen", "Thirty", "Forty"]
        both_scores_under_four = self.player1_score < 4 and self.player2_score < 4
        total_points_under_six = self.player1_score + self.player2_score < 6
        
        if both_scores_under_four and total_points_under_six:
            player1_score_str = score_map[self.player1_score]
            player2_score_str = score_map[self.player2_score]
            if self.player1_score == self.player2_score:
                return f"{player1_score_str}-All"
            return f"{player1_score_str}-{player2_score_str}"
        else:
            if self.player1_score == self.player2_score:
                return "Deuce"
            leading_player = self.player1_name if self.player1_score > self.player2_score else self.player2_name
            score_difference = abs(self.player1_score - self.player2_score)
            if score_difference == 1:
                return f"Advantage {leading_player}"
            return f"Win for {leading_player}"