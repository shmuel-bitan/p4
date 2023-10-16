import json
from models.player import Player
from view.player import create_player_view


def load_player_by_id(player_id):
    player_manager = PlayerManager("players.json")
    all_players = player_manager.load_players_from_json()
    player_manager.players = []
    for player in all_players:
        if player['id'] == player_id:
            return player
    return None


def new_player():
    player_manager = PlayerManager("players.json")
    # Create and add players
    player = create_player_view()
    player_manager.add_player(player)
    print(player)
    player_manager.save_player(player)


class PlayerManager:
    def __init__(self, filename):
        self.players = []
        self.filename = filename

    def add_player(self, player):
        self.players.append(player)

    def save_player(self, player):
        player_data = {
            "id": player.id,
            "name": player.name,
            "family_name": player.family_name,
            "date_of_birth": player.date_of_birth,
            "rank": player.rank,
            "score": player.score
        }
        self.save_to_json(player_data)

    def save_to_json(self, data):
        filename = "players.json"
        try:
            existing_data = self.load_players_from_json()
        except FileNotFoundError:
            existing_data = []

        existing_data.append(data)

        with open(filename, 'w') as file:
            json.dump(existing_data, file, indent=4, separators=(',', ': '))

    def modify_player_score(self, player_id, new_score):

        player = self.get_player_by_id(player_id)
        player['score'] = new_score
        self.players.append(player)

    def get_player_by_id(self, id_player):
        for player in self.players:
            if player.id == id_player:
                return player
        return None

    def load_players_from_json(self):
        try:
            with open(self.filename, 'r') as file:
                existing_player_data = json.load(file)
                # Create player objects from loaded data
                self.players = [
                    Player(data["id"], data["name"], data["family_name"], data["date_of_birth"], data["rank"])
                    for data in existing_player_data
                ]
                return existing_player_data
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. No players loaded.")
            return []


"""player_manager = PlayerManager("players.json")
player_manager.players = player_manager.load_players_from_json()
print(player_manager.players)
modify_player_score('12QWERT',5)
print(player_manager.get_player_by_id('12QWERT'))

player_manager = PlayerManager("players.json")
player_manager.load_players_from_json()
print(player_manager.players)
print(player_manager.get_player_by_id('AZ12345'))
"""
