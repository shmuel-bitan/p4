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


def get_date_time_tournament():
    tournament_id = input("rentrez l id du tournoi ")
    try:

        with open("tournaments.json", 'r') as file:
            tournaments = json.load(file)

        for tournament in tournaments:
            if tournament["id"] == tournament_id:
                print("le torunoi", tournament["name"], "a commence ", tournament["date"], "et a fini",
                      tournament["time_control"])
                return {
                    "name": tournament["name"],
                    "date": tournament["date"],
                    "time_control": tournament["time_control"]
                }

        return None
    except FileNotFoundError:
        print("Tournaments file not found.")
        return None


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
    sorted_players = sorted(players_data, key=lambda player: player.get("name", "").lower())
    return sorted_players


def print_all_player_alpha():
    """afficher les joueurs (appel de la focntion pour la view.py"""
    data_json = load_players_from_json("players.json")

    all_players_alphabetical = get_all_players_alphabetical(data_json)
    print("All players ordered by name:")
    for p in all_players_alphabetical:
        print(p)


def get_players_in_tournament_alphabetical():
    tournament_id = input("rentrez l id du tournoi ")
    try:
        with open("tournaments.json", 'r') as file:
            tournaments = json.load(file)

        for tournament in tournaments:
            if tournament["id"] == tournament_id:
                players_data = tournament['players']
                sorted_players = sorted(players_data, key=lambda player: player.get("name", "").lower())
                print("les joueurs", sorted_players)
    except FileNotFoundError:
        print("Tournaments file not found.")
        return None


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


def get_players_and_rounds_in_tournament():
    tournament_name = input("rentrez l id du tournoi")
    tournaments_data = load_tournaments_from_json("rounds.json")
    """"recup tout les rounds et joueurs dun tournoi"""
    for round in tournaments_data:
        if round["Tournament_Id"] == tournament_name:
            print(round)
        print("les rounds", round)
    return {}
