import random
import json
from ctrl.rounds import RoundManager
from ctrl.playermanager import PlayerManager, load_player_by_id
from models.tournament import Tournament
from view.player import check_id
from view.tournament import create_tournament_view


def play_tournament():
    player_added = 0
    current_round = 1
    player_manager = PlayerManager('players.json')
    current_tournament = TournamentManager(player_manager)
    tournament_to_add = create_tournament_view()
    tournament_id = tournament_to_add.get_id()
    nb_players = tournament_to_add.get_nb_players()
    tournament_round_number = tournament_to_add.get_nb_round()
    while player_added < nb_players:
        print("on ajoute le joueur ", player_added + 1)
        id_player = check_id()
        player_to_add = load_player_by_id(id_player)
        print(player_to_add)
        player_manager.add_player(player_to_add)
        player_added += 1
    print(player_manager.players)
    tournament_to_add.set_players(player_manager.players)
    current_tournament.add_tournament(tournament_to_add)
    while current_round < tournament_round_number + 1:
        print("on joue le round numero", current_round)
        current_tournament.play_round(tournament_id, current_round)
        current_round += 1
    current_tournament.save_tournament(tournament_to_add)


class TournamentManager:
    def __init__(self, player_manager):
        self.players = player_manager
        self.tournaments = []

    """def round_to_play(self, tournament_id, nb_rounds):
        round_number = 0
        while round_number < nb_rounds:
            round_number += 1
            print("on joue le round", round_number)
            if round_number == 1:
                self.play_round(tournament_id, round_number)
            else:
                self.play_round(tournament_id, round_number)
    """

    def add_tournament(self, tournament):

        self.tournaments.append(tournament)

    def load_tournament_from_json(self):
        try:
            with open("tournaments.json", 'r') as file:
                existing_player_data = json.load(file)
                # Create player objects from loaded data
                self.tournaments = [
                    Tournament(data["id"], data["name"], data["place"], data["date"], data["time_control"],
                               data["nb_players"], data["desc"], data["players"], data["nb_rounds"])
                    for data in existing_player_data
                ]
                return existing_player_data
        except FileNotFoundError:
            print("File tournaments.json not found. No players loaded.")
            return []

    def save_tournament(self, tournament):
        tournament_data = {
            "id": tournament.id,
            "name": tournament.name,
            "place": tournament.place,
            "date": tournament.date,
            "time_control": tournament.time_control,
            "nb_players": tournament.nb_players,
            "desc": tournament.desc,
            "players": tournament.players,
            "nb_rounds": tournament.nb_rounds
        }
        self.save_to_json(tournament_data)

    def save_to_json(self, data):
        filename = "tournaments.json"
        print(data)
        try:
            existing_data = self.load_tournament_from_json()
        except FileNotFoundError:
            existing_data = []

        existing_data.append(data)

        with open(filename, 'w') as file:
            json.dump(existing_data, file, indent=4, separators=(',', ': '))

    def get_tournaments_by_id(self, id):
        for tournament in self.tournaments:
            if tournament.id == id:
                return tournament
        return None

    def organize_pairs(self, randomize=True):
        pairs = []

        if randomize:
            random.shuffle(self.players.players)  # Randomly shuffle the player list
        pairs = [(self.players.players[i], self.players.players[i + 1]) for i in range(0, len(self.players.players), 2)]

        return pairs

    """def organize_pairs_by_score(self):
        sorted_players = sorted(self.players.players, key=lambda player: player['score'])
        pairs = [(sorted_players[i], sorted_players[i + 1]) for i in range(0, len(sorted_players), 2)]
        return pairs
"""

    def organize_pairs_by_score(self):
        sorted_players = sorted(self.players.players, key=lambda player: player.get("score", 0), reverse=True)
        pairs = [(sorted_players[i], sorted_players[i + 1]) for i in range(0, len(sorted_players), 2)]
        return pairs

    def play_round(self, tournament_id, round_number):
        if not self.players.players:
            print("No players in the tournament.")
            return []

        if len(self.players.players) % 2 != 0:
            print("Odd number of players. Cannot proceed.")
            return []

        if round_number == 1:
            print("bienvenu dans le round 1 du tournoi d echec ")
            pairs = self.organize_pairs(randomize=True)
        else:
            print("bienvenu dans le round ", round_number, "du tournoi d echec ")
            pairs = self.organize_pairs_by_score()

        round_results = []

        for pair in pairs:
            match = RoundManager("rounds.json")
            match_result = match.play_match(pair[0], pair[1], tournament_id, round_number)
            round_results.append(match_result)
            print(round_results)

        return round_results
    # recuperert id tournoi et numeero de round et enregistrer sur le json pour le rapport


# Example usage
if __name__ == "__main__":
    play_tournament()
