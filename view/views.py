from ctrl.playermanager import new_player, PlayerManager
from ctrl.rapports import get_all_players_alphabetical, print_all_player_alpha, print_all_tournament
from ctrl.tournament import TournamentManager

player_manager = PlayerManager("players.json")
tournament_manager = TournamentManager("tournaments.json")


def create_player():
    new_player()


def see_all_players():
    get_all_players_alphabetical()


def create_tournament(self):
    print("rien")


def modify_tournament(self):
    print("\nModify Tournament")


def menu():
    print("\nMain Menu:")
    print("1. Create Player")
    print("2. voir tout les joueurs ")
    print("3. creer un tournoi")
    print("4. voir un tournoi")
    print("5.voir tout les tournois")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        new_player()
    elif choice == "2":
        print_all_player_alpha()
    elif choice == "3":
        create_tournament()
    elif choice == "4":
        modify_tournament()
    elif choice == "5":
        print_all_tournament()

    else:
        print("Invalid choice. Please choose again.")


menu()