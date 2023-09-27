import json


class Tournament:
    def __init__(self, id, name, place, date, time_control, nb_players, desc, nb_rounds=4):
        self.id = id
        self.name = name
        self.place = place
        self.date = date
        self.time_control = time_control
        self.nb_players = nb_players
        self.nb_rounds = nb_rounds
        self.desc = desc
        self.players = []

    def set_players(self, player_list):
        self.players = player_list

    def add_players_by_id(self, player_ids, player_manager):
        for player_id in player_ids:
            player = player_manager.get_player_by_id(player_id)
            if player:
                self.players.append(player)
            else:
                print(f"Player with ID {player_id} not found.")

    def get_serialized_tournament(self):
        tournament_data = {
            "id": self.id,
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "time_control": self.time_control,
            "nb_players": self.nb_players,
            "nb_rounds": self.nb_rounds,
            "desc": self.desc,
            "players": [player.id for player in self.players]
        }
        return json.dumps(tournament_data, indent=4)

    @classmethod
    def load_from_json(cls, data):
        tournament = cls(
            data["id"],
            data["name"],
            data["place"],
            data["date"],
            data["time_control"],
            data["nb_players"],
            data["nb_rounds"],
            data["desc"]
        )
        return tournament
