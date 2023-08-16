class CreatePlayer():

    def menu(self):
        name = input("""Nom du joueur:\n> """)

        first_name = input("""Prénom du joueur:\n> """)

        date_of_birth = input("""date de naissance du joueur:\n> """)

        id = input("""ID du joueur:\n> """)

        rank = input("""rang du joueur:\n> """)

        print(f"Joueur {first_name} {name} créé.")

        return {
            "name": name,
            "first_name": first_name,
            "date_of_birth": date_of_birth,
            "id": id,
            "total_score": 0,
            "rank": rank,
        }
