from models.player import *
from ctrl.playermanager import *
from models.tournament import Tournament
from ctrl.tournament import TournamentManager


class Menu:
    def __init__(self):
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()

    def show_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Create Player")
            print("2. Modify Player")
            print("3. Create Tournament")
            print("4. Modify Tournament")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_player()
            elif choice == "2":
                self.modify_player()
            elif choice == "3":
                self.create_tournament()
            elif choice == "4":
                self.modify_tournament()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please choose again.")

    def create_player(self):
        print("\nCreate Player")
        # Implement player creation logic here

    def modify_player(self):
        print("\nModify Player")
        # Implement player modification logic here

    def create_tournament(self):
        print("\nCreate Tournament")
        # Implement tournament creation logic here

    def modify_tournament(self):
        print("\nModify Tournament")
        # Implement tournament modification logic here


if __name__ == "__main__":
    menu = Menu()
    menu.show_menu()
