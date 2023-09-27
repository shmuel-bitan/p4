"""json"""
import json


def load_players_from_json(filename):
    """charger tout les joueurs d un json"""
    try:
        with open(filename, 'r') as file:
            players_data = json.load(file)
            return players_data
    except FileNotFoundError:
        print(f"File '{filename}' not found. No players loaded.")
        return []


def load_tournaments_from_json(filename):
    """charger les tournois du json"""
    try:
        with open(filename, 'r') as file:
            tournaments_data = json.load(file)
            return tournaments_data
    except FileNotFoundError:
        print(f"File '{filename}' not found. No tournaments loaded.")
        return []


def get_all_players_alphabetical(players_data):
    """recuperer les joueurs et les triers par ordre alphabetique """
    sorted_players = sorted(players_data, key=lambda player: player['name'])
    return sorted_players


def print_all_player_alpha():
    """afficher les joueurs (appel de la focntion pour la view.py"""
    data_json = load_players_from_json("players.json")

    all_players_alphabetical = get_all_players_alphabetical(data_json)
    print("All players ordered by name:")
    for p in all_players_alphabetical:
        print(p)


def get_players_in_tournament_alphabetical(
        tournament_name, tournaments_data, players_data):
    """recup tout les joueurs du tournoi par ordre alphabetique"""
    for tournament in tournaments_data:
        if tournament['name'] == tournament_name:
            player_ids = tournament['players']
            players_in_tournament = [
                player for player in players_data if player['id'] in player_ids]
            sorted_players = sorted(
                players_in_tournament,
                key=lambda player: player['name'])
            return sorted_players
    return []


def get_all_tournaments(tournaments_data):
    """recup tout les tournois"""
    return tournaments_data


def print_all_tournament():
    """affiche tout les tournoi(raccourci pour view.py)"""
    tournaments_data = load_tournaments_from_json("tournaments.json")
    all_tournaments = get_all_tournaments(tournaments_data)
    print("All tournaments:")
    for tournament in all_tournaments:
        print(tournament)


def get_players_and_rounds_in_tournament(tournament_name, tournaments_data):
    """"recup tout les rounds et joueurs dun tournoi"""
    for tournament in tournaments_data:
        if tournament['name'] == tournament_name:
            return {
                'players': tournament['players'],
                'rounds': tournament['rounds']
            }
    return {}


# Example usage (You can call these functions as needed in your application)
if __name__ == "__main__":
    # Load player and tournament data from JSON files
    players_data = load_players_from_json("players.json")
    tournaments_data = load_tournaments_from_json("tournaments.json")

    # Example 1: Get all players ordered by name in alphabetical order
    print_all_player_alpha()

    # Example 2: Get all players from a tournament ordered by name in
    # alphabetical order
    TOURNAMENT_NAME = "Tournament1"  # Replace with the desired tournament name
    players_in_tournament = get_players_in_tournament_alphabetical(
        TOURNAMENT_NAME, tournaments_data, players_data)
    print(f"All players in '{TOURNAMENT_NAME}' ordered by name:")
    for player in players_in_tournament:
        print(player)

    # Example 3: Get all tournaments
    print_all_tournament()
    # Example 4: Get all players and rounds in a tournament

    players_and_rounds = get_players_and_rounds_in_tournament(
        TOURNAMENT_NAME, tournaments_data)
    print(f"All players and rounds in '{TOURNAMENT_NAME}':")
    print(players_and_rounds)
