
from ctrl.player import create_player

def menu():
    choice = int(input("que voulez vous faire"))
    if choice == 1:
        create_player()
    if choice == 2:
        print("2")
