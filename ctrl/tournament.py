import random
import json
from models.rounds import Match
from ctrl.playermanager import PlayerManager
from models.tournament import Tournament


class TournamentManager:
    def __init__(self, player_manager):
        self.players = player_manager
        self.tournaments = []
        print(self.players)

    """def create_tournament(self,id, name, place, start_time, end_time, nb_turn, desc):
        tournament = {
            "id": id,
            "name": name,
            "place": place,
            "start_time": start_time,
            "end_time": end_time,
            "nb_turn": nb_turn,
            "desc": desc,
        }
        self.tournaments.append(tournament)
    """

    def round_to_play(self, tournament_id, nb_rounds):
        round_number = 0
        while round_number < nb_rounds:
            round_number += 1
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

        with open("tournaments.json", 'w') as file:
            json.dump(tournament_data, file, indent=4)

    def get_tournaments_by_id(self, id):
        for tournament in self.tournaments:
            if tournament.id == id:
                return tournament
        return None

    def organize_pairs(self, randomize=True):
        pairs = []

        if randomize:
            random.shuffle(self.players)  # Randomly shuffle the player list
        pairs = [(self.players[i], self.players[i + 1]) for i in range(0, len(self.players), 2)]

        return pairs

    def organize_pairs_by_score(self):
        sorted_players = sorted(self.players, key=lambda player: player.score, reverse=True)
        pairs = [(sorted_players[i], sorted_players[i + 1]) for i in range(0, len(sorted_players), 2)]
        return pairs

    def play_round(self, tournament_id, round_number):
        if not self.players:
            print("No players in the tournament.")
            return []

        if len(self.players) % 2 != 0:
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
            match = Match(pair[0], pair[1], tournament_id)
            match.play_match()
            match_result = match.get_match_result()
            round_results.append(match_result)
            print(round_results)

        return round_results
    # recuperert id tournoi et numeero de round et enregistrer sur le json pour le rapport


# Example usage
if __name__ == "__main__":
    player_manager = PlayerManager("players.json")
    player_manager.load_players_from_json()

    # Create a tournament manager
    tournament_manager = TournamentManager(player_manager)

    # Create a new tournament
    t1 = Tournament(2, "tournoi d echec", "Paris", 23 - 10 - 2023, 25 - 10 - 2023, 2, "un tournoi")
    tournament_manager.add_tournament(
        t1
    )

    # Save the tournament to a JSON file
    tournament_manager.save_tournament()

    # Modify the tournament (change the description)

    # Create and add players with scores using PlayerManager
    player_manager = PlayerManager("players.json")
    player_manager.load_players_from_json()

    # Create and add players to the tournament
    player1 = player_manager.get_player_by_id(5)
    player2 = player_manager.get_player_by_id(6)
    player3 = player_manager.get_player_by_id(7)
    player4 = player_manager.get_player_by_id(8)
    player_manager.add_player(player2)
    player_manager.add_player(player3)
    player_manager.add_player(player4)
    player_manager.add_player(player1)

    tournament_manager = TournamentManager([player1, player2, player3, player4])

    tournament_manager.round_to_play(4)
