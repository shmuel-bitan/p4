import json
from models.player import *
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
        with open(self.filename, 'a') as file:
            json.dump(player_data, file)
            file.write('\n')

    def get_player_by_id(self, id):
        for player in self.players:
            if player.id == id:
                return player
        return None


    def load_players_from_json(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    player_data = json.loads(line.strip())
                    player = Player(player_data["id"], player_data["name"], player_data["family_name"],
                                    player_data["date_of_birth"], player_data["rank"])
                    player.score = player_data.get("score", 0)
                    # print(player.id , player.name)
                    # self.players.append(player)

        except FileNotFoundError:
            print(f"File '{self.filename}' not found. No players loaded.")

# Example usage
if __name__ == "__main__":

    player_manager = PlayerManager("players.json")

    player_manager.load_players_from_json()
    # Create and add players
    player1 = Player(1, "Jo", "Drey", "1990-01-15", "22")
    player1.score = 2
    player2 = Player(3, "m", "mr", "1985-03-20", "4")
    player2.score = 1
    player3 = Player(2, "m", "mt", "1985-03-20", "4")
    player3.score = 1
    player4 = Player(4, "m", "moi", "1985-03-20", "4")
    player4.score = 1
    player_manager.add_player(player1)
    player_manager.save_player(player1)
    player_manager.add_player(player2)
    player_manager.add_player(player3)
    player_manager.add_player(player4)
    for player in player_manager.players:
        player_manager.save_player(player)
        print(player)


    # Get a player by ID
    search_id = 1
    found_player = player_manager.get_player_by_id(search_id)

    if found_player:
        print("Player found:")
        print(found_player)
    else:
        print("Player not found.")