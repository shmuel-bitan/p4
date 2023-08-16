import json

from models.player import Player
from vues.player import *


def create_player():
    # Récupération des infos du joueur
    user_entries = create_player_view()

    # Création du joueur
    player = Player(
        user_entries['name'],
        user_entries['first_name'],
        user_entries['date_of_birth'],
        user_entries['id'],
        user_entries['total_score'],
        user_entries['rank'])
    print(player)
    serialized_player = Player.get_serialized_player(player)
    save_player(serialized_player)


def save_player(serialized_player):
    jsonString = json.dumps(serialized_player)
    jsonFile = open("player.json", "w")
    jsonFile.append(jsonString)
    jsonFile.close()
