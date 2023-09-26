import re
from models.player import Player


def check_date_of_birth():
    dob = input("rentrez une date de naissance dans le format JJ-MM-AAAA ")
    if not re.match(r'[0-9]{2}-[0-9]{2}-[0-9]{4}', dob):
        print("une daste respectant le format JJ-MM-AAAA ")
        return check_date_of_birth()
    return dob


def check_input():
    name = input("rentrez un nom ")
    if not name.isalpha():
        print("Uniquement des caractere alphabetique ")
        return check_input()
    return name


def check_id():
    id = input(" rentrez l identifiant national d echec du joueur ")
    if not re.match(r'[A-Z]{2}[0-9]{5}', id):
        check_id()
    return id


def check_rank():
    rank = input("rentrez un rank ")
    rank_int = int(rank)
    if not rank.isnumeric():
        print("Uniquement des chiffres et un rank valide  ")
        return check_rank()
    if rank.isnumeric() and rank_int > 3000:
        print("Uniquement des chiffres et un rank valide  ")
        return check_rank()

    return rank


def create_player_view():
    name = check_input()
    first_name = check_input()

    date_of_birth = check_date_of_birth()

    id = check_id()

    rank = check_rank()

    print(f"Joueur {first_name} {name} créé.")
    player = Player(id, name, first_name, date_of_birth, rank)
    return player


