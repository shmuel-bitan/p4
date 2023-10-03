import json
from models.rounds import Match
from models.player import Player


class RoundManager:
    def __init__(self, filename):
        self.rounds = []
        self.filename = filename

    def __str__(self):
        return self.rounds

    def add_rounds(self, round_to_add):
        self.rounds.append(round_to_add)

    def get_round_by_id(self, id_round):
        for nb_round in self.rounds:
            if nb_round.id == id_round:
                return nb_round
        return None

    def play_match(self, player1, player2, tournament_id, round_number):
        match = Match(player1, player2)
        match_result = match.play_match(player1, player2, tournament_id, round_number)
        self.rounds.append(match_result)
        self.save_round()
        return match_result

    def get_match_result(self, tournament_id, round_number):
        for result in self.rounds:
            if result["Tournament_Id"] == tournament_id and result["Round_Number"] == round_number:
                return result
        return None

    def save_round(self):
        with open(self.filename, 'a') as file:
            json.dump(self.rounds, file, indent=4)


player1 = Player("AZ12345","shmuel","bitan",24-10-2005,2000,0)
player2 = Player("AZ12445","shmuel","bitan",24-10-2005,2000)
id = 1
r = 2

def play_round_get_result(player1, player2, id_tournament, round_number):
    current_round_gestion = RoundManager("rounds.json")
    current_round_gestion.play_match(player1, player2, id_tournament, round_number)

