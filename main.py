from ctrl.player import create_player


def main():
    choice = int(input("que voulez vous faire"))
    if choice == 1:
        create_player()


main()