from ctrl.playermanager import new_player, PlayerManager, load_player_by_id
from ctrl.rapports import get_all_players_alphabetical, print_all_player_alpha, print_all_tournament, \
    get_date_time_tournament
from ctrl.tournament import TournamentManager, play_tournament

player_manager = PlayerManager("players.json")
tournament_manager = TournamentManager("tournaments.json")


def create_player():
    new_player()


def see_all_players():
    get_all_players_alphabetical()


def create_tournament():
    play_tournament()


def date_tournament():
    get_date_time_tournament()


def menu():
    print("\nMain Menu:")
    print("1. Create Player")
    print("2. liste de tous les joueurs par ordre alphabétique ")
    print("3. creer un tournoi")
    print("4. nom et dates d’un tournoi donné")
    print("5.liste de tous les tournois")
    print("6. liste des joueurs du tournoi par ordre alphabétique")
    print("7.liste de tous les tours du tournoi et de tous les matchs du tour")
    choice = input("Enter your choice: ")

    if choice == "1":
        new_player()
    elif choice == "2":
        print_all_player_alpha()
    elif choice == "3":
        create_tournament()
    elif choice == "4":
        date_tournament()
    elif choice == "5":
        print_all_tournament()
    elif choice == "6":
        print_all_tournament()
    elif choice == "7":
        print_all_tournament()

    else:
        print("Invalid choice. Please choose again.")


