import json
import unittest

class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.player1_total_points = 0
        self.player2_total_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
            self.player1_total_points += 1
        elif player_name == self.player2_name:
            self.player2_score += 1
            self.player2_total_points += 1
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
        
    def get_total_points(self):
        return self.player1_total_points, self.player2_total_points

def play_game(TennisGameClass, p1_points, p2_points, p1_name, p2_name):
    game = TennisGameClass(p1_name, p2_name)
    for _ in range(p1_points):
        game.won_point(p1_name)
    for _ in range(p2_points):
        game.won_point(p2_name)
    return game

class TestGoldenMaster(unittest.TestCase):
    def setUp(self):
        with open('golden_master.json', 'r') as file:
            self.golden_master = json.load(file)
    
    def test_against_golden_master(self):
        for key, expected_score in self.golden_master.items():
            p1_name, p2_name, p1_points, p2_points = key.split('-')
            p1_points, p2_points = int(p1_points), int(p2_points)
            game = play_game(TennisGame3, p1_points, p2_points, p1_name, p2_name)
            self.assertEqual(expected_score, game.get_score())