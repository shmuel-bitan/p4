import json


class RoundManager:
    def __init__(self, filename):
        self.rounds = []
        self.filename = filename

    def add_rounds(self, round_to_add):
        self.rounds.append(round_to_add)

    def get_round_by_id(self, id_round):
        for nb_round in self.rounds:
            if nb_round.id == id_round:
                return nb_round
        return None

    def get_match_result(self, tournament_id, round_number):
        for result in self.rounds:
            if result["Tournament_Id"] == tournament_id and result["Round_Number"] == round_number:
                return result
        return None

    def save_round(self):
        with open(self.filename, 'w') as file:
            json.dump(self.rounds, file, indent=4)
