import re
from models.tournament import Tournament


def check_tournament_name():
    name = input("Enter the tournament name: ")
    if not re.match(r'^[A-Za-z0-9\s]+$', name):
        print("Invalid tournament name. Please use alphanumeric characters and spaces.")
        return check_tournament_name()
    return name


def check_tournament_place():
    place = input("Enter the tournament place: ")
    if not re.match(r'^[A-Za-z\s]+$', place):
        print("Invalid tournament place. Please use alphabetic characters and spaces.")
        return check_tournament_place()
    return place


def check_date():
    date = input("Entrez une date au format JJ-MM-AAA: ")
    if not re.match(r'[0-9]{2}-[0-9]{2}-[0-9]{4}$', date):
        print("Format invalide.")
        return check_date()
    return date


def check_nb_players():
    nb_players = input("Enter the number of players: ")
    if not nb_players.isdigit() or int(nb_players) < 2:
        print("Invalid number of players. Please enter a valid positive integer (minimum 2 players).")
        return check_nb_players()
    return int(nb_players)


def check_nb_rounds():
    nb_rounds = input("Enter the number of rounds: ")
    if nb_rounds == '':
        nb_rounds = 4
        print("le nombre de round est initialisé a 4")
    elif not nb_rounds.isdigit() or int(nb_rounds) < 1:
        print("Invalid number of rounds. Please enter a valid positive integer (minimum 1 round).")
        return check_nb_rounds()
    return int(nb_rounds)


def check_tournament_description():
    desc = input("Enter a tournament description: ")
    return desc


def check_id():
    id = input("rentrez l id du tournoi")
    return id


def create_tournament_view():
    print("Create a new tournament:")

    name = check_tournament_name()
    place = check_tournament_place()
    date = check_date()
    time_control = check_date()
    nb_players = check_nb_players()
    nb_rounds = check_nb_rounds()
    desc = check_tournament_description()
    id = check_id()

    print(f"Tournament '{name}' created.")
    print(nb_rounds)
    tournament = Tournament(id, name, place, date, time_control, nb_players, desc, 0, nb_rounds)

    return tournament
