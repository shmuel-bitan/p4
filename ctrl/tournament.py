import random
import json
from models.rounds import Match
from ctrl.rounds import RoundManager
from ctrl.playermanager import PlayerManager, load_player_by_id
from models.tournament import Tournament
from view.player import check_id
from view.tournament import create_tournament_view


def play_tournament():
    player_added = 0
    current_round = 0
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
    while tournament_round_number > current_round:
        print("on joue le round numero", current_round+1)
        current_tournament.play_round(tournament_id, current_round)
        current_round += 1
    current_tournament.save_tournament()


class TournamentManager:
    def __init__(self, player_manager):
        self.players = player_manager
        self.tournaments = []

    def round_to_play(self, tournament_id, nb_rounds):
        round_number = 0
        while round_number < nb_rounds:
            round_number += 1
            print("on joue le round", round_number)
            if round_number == 1:
                self.play_round(tournament_id, round_number)
            else:
                self.play_round(tournament_id, round_number)

    def add_tournament(self, tournament):

        self.tournaments.append(tournament)

    def save_tournament(self):
        tournament_data = [
            {
                "id": tournament.id,
                "name": tournament.name,
                "place": tournament.place,
                "date": tournament.date,
                "time_control": tournament.time_control,
                "nb_players": tournament.nb_players,
                "nb_rounds": tournament.nb_rounds,
                "desc": tournament.desc,
                "players": tournament.players
            }
            for tournament in self.tournaments
        ]

        with open("tournaments.json", 'a') as file:
            json.dump(tournament_data, file, indent=4)

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

    def organize_pairs_by_score(self):
        sorted_players = sorted(self.players.players, key=lambda player: player['score'])
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
