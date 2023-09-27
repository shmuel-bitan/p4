import json


class Player:
    def __init__(self, id, name, family_name, date_of_birth, rank):
        self.id = id
        self.name = name
        self.family_name = family_name
        self.date_of_birth = date_of_birth
        self.rank = rank
        self.score = 0  # A list to store the player's tournament scores

    def get_score(self):
        return self.score

    def __str__(self):
        return f"{self.name} {self.family_name}, Score: {self.get_score()}"

    def get_serialized_player(self):
        player_data = {
            "id": self.id,
            "name": self.name,
            "family_name": self.family_name,
            "date_of_birth": self.date_of_birth,
            "rank": self.rank,
            "tournaments": self.score
        }
        return json.dumps(player_data, indent=4)
