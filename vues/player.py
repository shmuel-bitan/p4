def only_name():
    s = input("Entrez le nom du joueur : ")
    if not s.isalpha():
        print("Uniquement des caractere alphabetique ")
        only_name()
    else:
        return s
def menu():
        name = only_name()

        first_name = input("""Prénom du joueur:\n> """)

        if not first_name.isalpha():
            print("le prenom doit contenir uniquement des caratere alphabetique.")
            first_name = input("""Prénom du joueur:\n> """)
        date_of_birth = input("""date de naissance du joueur:\n> """)

        id = input("""ID du joueur:\n> """)

        rank = int(input("""rang du joueur:\n> """))

        print(f"Joueur {first_name} {name} créé.")

        return {
            "name": name,
            "first_name": first_name,
            "date_of_birth": date_of_birth,
            "id": id,
            "total_score": 0,
            "rank": rank,
        }
