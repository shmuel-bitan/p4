from ctrl.playermanager import modify_player_score


class Match:
    def __init__(self, player1, player2, tournament_id, round_number):
        self.player1 = player1
        self.player2 = player2
        self.tournament_id = tournament_id
        self.round_number = round_number

    def play_match(self, player1, player2, tournament_id, round_number):
        print(f"{player1.name} vs. {player2.name}")
        outcome = input("Enter the outcome (1 for Player 1 win, 2 for Player 2 win, 0 for draw): ")

        if outcome == "1":
            player1.score += 1
            modify_player_score(player1, player1.score)
        elif outcome == "2":
            player2.score += 1
            modify_player_score(player2, player2.score)
        elif outcome == "0":
            player1.score += 0.5
            player2.score += 0.5
            modify_player_score(player1, player1.score)
            modify_player_score(player2, player2.score)

        match_result = {
            "Tournament_Id": tournament_id,
            "Player1 ID": player1.id,
            "Player1 Score": player1.score,
            "Player2 ID": player2.id,
            "Player2 Score": player2.score,
            "Round_Number": round_number
        }

        return match_result

    def __str__(self):
        return {self.player1.name, self.player1.score, self.player2.name, self.player2.score, self.round_number}
