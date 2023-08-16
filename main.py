from ctrl.player import create_player
from models.player import Player


def menu():
    choice = int(input("que voulez vous faire"))
    if choice == 1:
        create_player()
    if choice == 2:
        print("2")


if __name__ == "__main__":
    menu()
