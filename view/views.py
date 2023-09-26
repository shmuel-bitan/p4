from ctrl.playermanager import new_player, PlayerManager
from ctrl.rapports import get_all_players_alphabetical
from ctrl.tournament import TournamentManager

player_manager = PlayerManager("players.json")
tournament_manager = TournamentManager("tournament.json")


def create_player():
    new_player()


def see_all_players():
    get_all_players_alphabetical()



def create_tournament(self):
 print("rien")

def modify_tournament(self):
    print("\nModify Tournament")


if __name__ == "__main__":
    print("\nMain Menu:")
    print("1. Create Player")
    print("2. voir tout les joueurs ")
    print("3. Create Tournament")
    print("4. Modify Tournament")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        new_player()
    elif choice == "2":
        get_all_players_alphabetical()
    elif choice == "3":
        create_tournament()
    elif choice == "4":
        modify_tournament()
    elif choice == "5":
        print("Exiting...")

    else:
        print("Invalid choice. Please choose again.")
