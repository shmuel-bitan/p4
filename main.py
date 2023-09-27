
from view.views import menu


if __name__ == "__main__":
    menu()

import unittest
from models.player import Player
from ctrl.playermanager import PlayerManager
from models.tournament import Tournament

class TestTournamentCreation(unittest.TestCase):
    def setUp(self):
        # Create a PlayerManager and add players with complete information
        self.player_manager = PlayerManager("players.json")

        self.player1 = Player(1, "John", "Doe", "1990-01-15", "Intermediate")
        self.player2 = Player(2, "Alice", "Smith", "1985-03-20", "Advanced")
        self.player3 = Player(3, "Bob", "Johnson", "1995-07-10", "Intermediate")
        self.player4 = Player(4, "Emily", "Brown", "1988-11-05", "Advanced")

        self.player_manager.add_player(self.player1)
        self.player_manager.add_player(self.player2)
        self.player_manager.add_player(self.player3)
        self.player_manager.add_player(self.player4)

    def test_create_tournament(self):
        # Create a tournament with 2 rounds and 4 players
        tournament = Tournament(
            id=1,
            name="Test Tournament",
            place="City X",
            date="2023-09-15",
            time_control="2023-06",
            nb_players=4,
            nb_rounds=2,
            desc="Description of the test tournament"
        )

        # Add players to the tournament by their IDs
        player_ids = [1, 2, 3, 4]
        tournament.add_players_by_id(player_ids, self.player_manager)

        # Assert that the tournament has the correct number of players
        self.assertEqual(len(tournament.players), 4)

if __name__ == "__main__":
    unittest.main()