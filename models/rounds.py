
import time
from models.player import Player

class Match:
    def __init__(self, player1, player2):
        self.player1 = Player(player1['id'],player1['name'],player1['family_name'],player1['date_of_birth'],player1['rank'],player1['score'])
        self.player2 = Player(player2['id'],player2['name'],player2['family_name'],player2['date_of_birth'],player2['rank'],player2['score'])
        self.match_start = None  # Initialize match_start to None
        self.match_end = None  # Initialize match_end to None

    def play_match(self, player1, player2, tournament_id, round_number):
        self.match_start = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{player1['name']} vs. {player2['name']}")
        outcome = input("Enter the outcome (1 for Player 1 win, 2 for Player 2 win, 0 for draw): ")

        if outcome == "1":
            player1['score'] += 1

        elif outcome == "2":
            player2['score'] += 1

        elif outcome == "0":
            player1['score'] += 0.5
            player2['score'] += 0.5
        self.match_end = time.strftime("%Y-%m-%d %H:%M:%S")

        match_result = {
            "Tournament_Id": tournament_id,
            "Player1 ID": player1['id'],
            "Player1 Score": player1['score'],
            "Player2 ID": player2['id'],
            "Player2 Score": player2['score'],
            "Round_Number": round_number,
            "start_time": self.match_start,
            "end_time": self.match_end
        }

        return match_result

    def __str__(self):
        return {self.player1.name, self.player1.score, self.player2.name, self.player2.score, self.round_number}
