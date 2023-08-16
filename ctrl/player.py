from models.player import Player
from vues.player import *


def create_player():
    # Récupération des infos du joueur
    user_entries = menu()

    # Création du joueur
    player = Player(
        user_entries['name'],
        user_entries['first_name'],
        user_entries['date_of_birth'],
        user_entries['id'],
        user_entries['total_score'],
        user_entries['rank'])
    print(player)


