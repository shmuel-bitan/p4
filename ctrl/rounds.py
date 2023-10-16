from models.rounds import Match


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
        return match_result

    def get_match_result(self, tournament_id, round_number):
        for result in self.rounds:
            if result["Tournament_Id"] == tournament_id and result["Round_Number"] == round_number:
                return result
        return None


def play_round_get_result(player1, player2, id_tournament, round_number):
    current_round_gestion = RoundManager("rounds.json")
    current_round_gestion.play_match(player1, player2, id_tournament, round_number)
