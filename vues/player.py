import re
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


def check_rank():
    rank = input("rentrez un rank ")
    if not rank.isnumeric():
        print("Uniquement des chiffres et un rank valide  ")
        return check_rank()
    if rank.isnumeric() and rank>3000:
        print("Uniquement des chiffres et un rank valide  ")
        return check_rank()

    return rank


def create_player_view():
    name = check_input()
    first_name = check_input()


    date_of_birth = check_date_of_birth()

    id = input("""ID du joueur:\n> """)

    rank = check_rank()

    print(f"Joueur {first_name} {name} créé.")

    return {
        "name": name,
        "first_name": first_name,
        "date_of_birth": date_of_birth,
        "id": id,
        "total_score": 0,
        "rank": rank,
    }
