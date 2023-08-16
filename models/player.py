
class Player:
    def __init__(
            self, name, first_name, date_of_birth, id, total_score, rank=0):
        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.id = id
        self.total_score = total_score
        self.tournament_score = 0
        self.rank = rank

    def __str__(self):
        return f"{self.first_name} {self.name} [{self.tournament_score} pts]"

    def get_serialized_player(self):
        serialized_player = {
            "name": self.name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "id": self.id,
            "total_score": self.total_score,
            "tournament_score": self.tournament_score,
            "rank": self.rank,
        }

        return serialized_player
